from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from blog.models import PostModel, BannerModel

def post(request, slug):
    post = get_object_or_404(PostModel, slug=slug)
    banner = BannerModel.objects.filter(active='True')
    context={
    'key' : 'value',
    'key1' : 'value1',
    'key2' : 'value2',
    }
    return render(request, 'blog.html', context)
