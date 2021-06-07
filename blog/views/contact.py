from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from blog.models import ContactModel, BannerModel

def contact(request):
    banner = BannerModel.objects.filter(active='True')
    context={
        'key' : 'value',
        'key1' : 'value1',
        'key2' : 'value2',
        'banners' : banner,
    }
    return render(request, 'contact.html', context)
