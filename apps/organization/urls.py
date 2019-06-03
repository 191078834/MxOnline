#!/usr/bin/python
# -*- coding: utf-8 -*-
#Auther: WQM
#Time: 2019/5/28 15:19
from django.urls import path,re_path, include
from .views import OrgView

# 一定要写上app的名字
app_name = 'organization'

urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list')
]