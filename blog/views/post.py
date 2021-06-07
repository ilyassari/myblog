from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from blog.models import PostModel, CommentModel, BannerModel

def post(request, slug):
    post = get_object_or_404(PostModel, slug=slug)
    comments = post.p_comments.all()
    banner = BannerModel.objects.filter(active='True')
    print(comments)
    context={
        'post' : post,
        'comments' : comments,
        'banners' : banner,
    }
    return render(request, 'one_post.html', context)
