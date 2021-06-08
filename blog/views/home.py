from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from blog.models import PostModel, CommentModel, BannerModel

def home(request):
    search = request.GET.get('sq')
    posts = PostModel.objects.order_by('-id')
    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search)
        ).distinct()
    banner = BannerModel.objects.filter(active='True')
    page = request.GET.get('pg')
    paginator = Paginator(posts, 6)
    context={
        'banners' : banner,
        'posts' : paginator.get_page(page),
    }
    return render(request, 'home.html', context)
