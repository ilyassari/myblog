from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from blog.models import PostModel, CommentModel, BannerModel

@login_required(login_url='/')
def my_posts(request):
    posts = request.user.a_post.order_by('-id')
    print(posts)
    banner = BannerModel.objects.filter(active='True')
    page = request.GET.get('pg')
    paginator = Paginator(posts, 6)
    context={
        'banners' : banner,
        'posts': paginator.get_page(page),
    }
    return render(request, 'my_posts.html', context)
