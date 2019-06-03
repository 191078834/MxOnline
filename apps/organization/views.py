from django.shortcuts import render
from django.views.generic.base import View
from .models import CityDict, CourseOrg, Teacher
from pure_pagination import PageNotAnInteger, Paginator
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

        print(category, '*******',city_id)
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
            'hot_orgs': hot_orgs,
            'sort': sort
        })