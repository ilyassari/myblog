from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from blog.models import CommentModel

@login_required(login_url='/')
def delete_comment(request, id):
    """ deleting a comment """
    # banner = BannerModel.objects.filter(active='True')
    comment = get_object_or_404(CommentModel, id=id, )
    if comment.author == request.user or comment.post.author == request.user:
        comment.delete()
        return redirect('post_page', slug=comment.post.slug)
    return redirect('home_page')
