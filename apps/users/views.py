from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForgetPsdForm
from django.contrib.auth.hashers import make_password
from utils. email_send import send_register_email
# Create your views here.

#邮箱和用户名都可以登录
# 基础ModelBackend类，因为它有authenticate方法
class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, requset):
        login_form = LoginForm(requset.POST)
        if login_form.is_valid():
            user_name = requset.POST.get('username', None)
            pass_word = requset.POST.get('password', None)
            # 成功返回user对象 失败返回None
            user = authenticate(user_name=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(requset, user)
                    return render(requset, 'index.html')
            else:
                return render(requset, 'login.html', {'msg': '用户名密码错误', 'login_form':login_form})
        else:
            # form.is_valid（）已经判断不合法了，所以这里不需要再返回错误信息到前端了
            return render(requset, 'login.html', {'login_form': login_form})


class ActiveUserView(View):
    def get(self, request, acvite_code):
        all_records = EmailVerifyRecord.objects.filter(code=acvite_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            render(request, 'active_fail.html')
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', None)
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form':register_form,'msg': '用户已存在'})
            pass_word = request.POST.get('password', None)
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            # 对保存到数据库的密码加密
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_email(user_name, 'register')
            return render(request, 'login.html', {'success_msg':'please go to Email'})
        else:
            return render(request, 'register.html', {'register_form':register_form})

class ForgertPwdVied(View):
    def get(self, request):
        forget_form = ForgetPsdForm()
        return render(request, 'forgetpwd.html', {'fogget_form':forget_form})
    def post(self, request):
        forget_form = ForgetPsdForm()
        if forget_form.is_valid():
            email = request.POST.get('email', None)
            send_register_email(email, send_type='forget')
            return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.htnl', {'forget_form':forget_form})

class ResetView(View):
    def get(self, request, actice_code):
        all_records = EmailVerifyRecord.objects.filter(code=actice_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email':email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')