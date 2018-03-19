import xadmin
from xadmin import views # 主题
from backend.models import *


class BaseSetting(object): # 设置主题
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = "Zero CMS"
    site_footer = "零科技"
    menu_style = "accordion" # 紧缩导航

class CinemaAdmin(object):
    list_display = ['name', 'address', 'price', 'brand', 'region', 'filmOffice', 'createTime', 'modifyTime', 'createUser']
    search_fields = ['name', 'address', 'price',  'brand__name', 'region__name', 'filmOffice__name','createTime', 'modifyTime']
    list_filter  = ['name', 'address', 'price',  'brand__name', 'region__name', 'filmOffice__name', 'createTime', 'modifyTime']

class BrandAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter  = ['name']

class RegionAdmin(object):
    list_display = ['name', 'province', 'city', 'country']
    search_fields = ['name', 'province', 'city', 'country']
    list_filter  = ['name', 'province', 'city', 'country']

class FilmOfficeAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter  = ['name']

xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(Cinema, CinemaAdmin)
xadmin.site.register(Brand, BrandAdmin)
xadmin.site.register(Region, RegionAdmin)
xadmin.site.register(FilmOffice, FilmOfficeAdmin)
