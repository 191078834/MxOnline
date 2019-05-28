from django.shortcuts import render
from django.views.generic.base import View
from .models import CityDict, CourseOrg, Teacher
# Create your views here.
class OrgView(View):
    '''课程机构'''
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_onums = all_orgs.count()
        all_citys = CityDict.objects.all()

        return render(request, "org-list.html", {
            "all_orgs": all_orgs,
            "all_citys": all_citys,
            'org_onums': org_onums,
        })