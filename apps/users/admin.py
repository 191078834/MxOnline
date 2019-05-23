from django.contrib import admin

# Register your models here.
from .models import EmailVerifyRecord, Banner
import xadmin

#xadmin中这里是继承object，不再是继承admin.ModelAdmin
class EmailVerifyRecordAdmin(object):

    list_display = ['code', 'email', 'send_time', 'send_type']
    # 搜索的字段 不要添加时间搜索
    search_fields = ['code', 'email','send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_time', 'send_type']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']

xadmin.site.register(Banner,BannerAdmin)
