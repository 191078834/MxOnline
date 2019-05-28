#!/usr/bin/python
# -*- coding: utf-8 -*-
#Auther: WQM
#Time: 2019/5/28 15:19
from django.urls import path,re_path
from .views import OrgView

app_names = 'organization'

urlpatterns = [
    path('org_list/',OrgView.as_view(),name='org_list'),
]