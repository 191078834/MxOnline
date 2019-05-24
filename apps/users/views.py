from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm
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
                login(requset, user)
                return render(requset, 'index.html')
            else:
                return render(requset, 'login.html', {'msg': '用户名密码错误', 'login_form':login_form})
        else:
            # form.is_valid（）已经判断不合法了，所以这里不需要再返回错误信息到前端了
            return render(requset, 'login.html', {'login_form': login_form})