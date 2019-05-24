#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Auther: WQM
#Time: 2019/5/24 13:52
import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 修改title
    site_title = 'NBA后台管理'
    # 修改底部 footer
    site_footer = '我的公司'
    # 收起菜单
    menu_style = 'accordion'


#xadmin中这里是继承object，不再是继承admin.ModelAdmin
class EmailVerifyRecordAdmin(object):

    list_display = ['code', 'email', 'send_time', 'send_type']
    # 搜索的字段 不要添加时间搜索
    search_fields = ['code', 'email','send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_time', 'send_type']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)

