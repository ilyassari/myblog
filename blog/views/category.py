from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from blog.models import PostModel, BannerModel, CategoryModel

def category(request, slug):
    category = get_object_or_404(CategoryModel, slug=slug)
    posts = category.c_post.order_by('-id')
    banner = BannerModel.objects.filter(active='True')
    page = request.GET.get('pg')
    paginator = Paginator(posts, 6)
    context={
        'category' : category.title,
        'banners' : banner,
        'posts' : paginator.get_page(page),
    }
    return render(request, 'category.html', context)
