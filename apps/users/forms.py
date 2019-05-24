#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/5/24 17:23
from django import forms

class LoginForm(forms.Form):
    # 用户名密码不能为空 密码最小长度为5
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
