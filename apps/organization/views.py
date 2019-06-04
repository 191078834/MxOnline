from django.shortcuts import render
from django.views.generic.base import View
from .models import CityDict, CourseOrg, Teacher
from pure_pagination import PageNotAnInteger, Paginator
from .forms import UserAskForm
from django.http import HttpResponse
# Create your views here.
class OrgView(View):
    '''课程机构'''
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_onums = all_orgs.count()
        all_citys = CityDict.objects.all()

        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct', '')

        if category:
            all_orgs = all_orgs.filter(category=category)

        # 热门课程排行
        hot_orgs = all_orgs.order_by('-click_nums')[:4]
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")

        print('排行:',sort, '类别:', category, '城市:', city_id)
        # 有多少家机构
        org_nums = all_orgs.count()

        # 分页神器 pure_pagination
        try:
            page = request.GET.get('page', 1)

        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 3, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_onums": org_onums,
            "city_id":city_id,
            "org_nums":org_nums,
            "category": category,
            'hot_orgs': hot_orgs,
            'sort': sort
        })

class AddUserAskView(View):
    '''
    用户添加咨询
    '''
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            # 如果commit=False 就是告诉Django先不要发送数据到数据库 可能会额外的添加一些数据之后
            user_ask = userask_form.save(commit=True)
            # 如果保存成功,返回json字符串,后面content type是告诉浏览器返回的数据类型
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')

class OrgHomeView(View):
    '''机构首页'''
    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=org_id)
        all_courses = course_org.course_set.all()[:4]
        all_teacher = course_org.teacher_set.all()[:2]
        return render(request, 'org-detail-homepage.html',
                      {'course_org': course_org, 'all_courses': all_courses, 'all_teacher': all_teacher
                       ,'current_page':current_page})

class OrgCourseView(View):
    """机构课程列表页"""
    def get(self, request, org_id):
        # 根据id取到课程机构
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 通过课程机构找到课程。内建的变量，找到指向这个字段的外键引用
        all_courses = course_org.course_set.all()

        return render(request, 'org-detail-course.html', {
            'all_courses': all_courses,
            'course_org': course_org , 'current_page':current_page})

class OrgDescView(View):
    '''机构介绍页'''
    def get(self, request, org_id):
        current_page = 'desc'
        # 根据id取到课程机构
        course_org = CourseOrg.objects.get(id= int(org_id))
        return render(request, 'org-detail-desc.html',{
            'course_org': course_org,
            'current_page':current_page,
        })

class OrgTeacherView(View):
    """ 机构教师页 """
    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id= int(org_id))
        all_teacher = course_org.teacher_set.all()

        return render(request, 'org-detail-teachers.html',{
           'all_teacher':all_teacher,
            'course_org': course_org,
            'current_page':current_page,
        })













