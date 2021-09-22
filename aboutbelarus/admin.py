from django.contrib import admin
from .models import *


class AboutBelarusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class UserSendMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'time_sending')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(AboutBelarus, AboutBelarusAdmin)
admin.site.register(UserSendMessage, UserSendMessageAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель сайта об интересных местах в Беларуси'
admin.site.site_header = 'Админ-панель сайта об интересных местах в Беларуси'
