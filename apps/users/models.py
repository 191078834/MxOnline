from django.db import models

# Create your models here.
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):

    gender_choices = (
        ('male','男'),
        ('female', '女')
    )

    nick_name = models.CharField('昵称', max_length=50, default='')
    birthday = models.DateField('生日', blank=True, null=True)
    gender = models.CharField('性别', choices=gender_choices, default='male', max_length=10)
    address = models.CharField('地址', null=True, blank=True, max_length=100)
    mobile = models.CharField('手机号', max_length=11, null=True,blank=True)
    image = models.ImageField('image/%Y%m', default='image/default.png', max_length=200)

    class Meta:
        # 指定在admin管理界面中显示中文
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):

    send_choices = (
        ('register', '注册'),
        ('forget', '找回密码')
    )

    code = models.CharField('验证码', max_length=20)
    email = models.EmailField('邮箱', max_length=50)
    send_type = models.CharField(choices=send_choices, max_length=10)
    send_time = models.DateTimeField('发送时间', default=datetime.now)

    class Meta:
       # 指定在admin管理界面中显示中文
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

# 轮播?
class Banner(models.Model):

    title = models.CharField('标题', max_length=100)
    image = models.ImageField('轮播图', upload_to='banner/%Y%m', max_length=100)
    url = models.URLField('访问地址', max_length=200)
    index = models.IntegerField('顺序', default=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name