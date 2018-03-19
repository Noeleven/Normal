from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Cinema(models.Model):
    name = models.CharField('影院名称', max_length=200)
    address = models.CharField('地址', max_length=300)
    price = models.IntegerField('价格')
    brand = models.ForeignKey('Brand', verbose_name='品牌')
    region = models.ForeignKey('Region', verbose_name='地区')
    filmOffice = models.ForeignKey('FilmOffice', verbose_name='影厅')
    createUser = models.ForeignKey(User, related_name='cinemas', on_delete=models.CASCADE)
    createTime = models.DateTimeField('创建时间', auto_now_add=True)
    modifyTime = models.DateTimeField('修改时间', auto_now=True)

    class Meta: # 用于配置后台显示的名称
        verbose_name = '影院'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField('品牌名称', max_length=200)

    class Meta:
        verbose_name = '影院品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField('地区', max_length=200)
    province = models.CharField('省', max_length=200)
    city = models.CharField('城市', max_length=200)
    country = models.CharField('国家', max_length=200)

    class Meta:
        verbose_name = '地区'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class FilmOffice(models.Model):
    name = models.CharField('影厅', max_length=200)

    class Meta:
        verbose_name = '影厅'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
    # def __int__(self):
    #     return self.id
# class CinemaAdmin(admin.ModelAdmin):
#     list_display = ('name', 'address', 'price', 'createTime', 'modifyTime')
#     search_fields = ['name', 'address', 'price', 'createTime', 'modifyTime']
#     list_filter  = ['name', 'address', 'price', 'createTime', 'modifyTime']
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ['name']
#     list_filter  = ['name']
# class RegionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'province', 'city', 'country')
#     search_fields = ['name', 'province', 'city', 'country']
#     list_filter  = ['name', 'province', 'city', 'country']
# class FilmOfficeAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ['name']
#     list_filter  = ['name']
#
# admin.site.register(Cinema, CinemaAdmin)
# admin.site.register(Brand, BrandAdmin)
# admin.site.register(Region, RegionAdmin)
# admin.site.register(FilmOffice, FilmOfficeAdmin)
