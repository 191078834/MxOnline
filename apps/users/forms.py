#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/5/24 17:23
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    # 用户名密码不能为空 密码最小长度为5
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

class RegisterForm(forms.Form):
    '''注册验证表单'''
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 验证码 字段里面可以自定义错误信息
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})

class ForgetPsdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})

class ModifyPwdFrom(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

