from django.contrib import admin
from blog.models import *

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_date', 'modified_date')

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_date', 'modified_date')

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'full_name', 'created_date')

@admin.register(BannerModel)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'active')
