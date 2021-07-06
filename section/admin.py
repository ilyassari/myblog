from django.contrib import admin
from section.models import *

# Register your models here.

@admin.register(BannerModel)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'active')
