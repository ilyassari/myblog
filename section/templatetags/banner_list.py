from django import template
from section.models import BannerModel

register = template.Library()

@register.simple_tag
def banner_list():
    banners = BannerModel.objects.filter(active='True')
    # banners = BannerModel.objects.all()
    return banners
