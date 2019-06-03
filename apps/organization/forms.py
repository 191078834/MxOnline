#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/6/3 17:24
from django import forms
from operation.models import UserAsk

class UserAskForm(forms.Form):
    class Meta:
        model = UserAsk
        fileds = ['name', 'mobile', 'course_name']

