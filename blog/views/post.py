from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from blog.models import PostModel, CommentModel, BannerModel
from blog.forms import AddPostForm, UpdatePostForm, AddCommentForm

banner = BannerModel.objects.filter(active='True')

def post(request, slug):
    """ viewing post detail """
    post = get_object_or_404(PostModel, slug=slug)
    comments = post.p_comments.all()
    if request.method == 'POST':
        comment_form = AddCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
        return redirect('post_page', slug=post.slug)
    else:
        comment_form = AddCommentForm()
    lposts =  PostModel.objects.order_by('-modified_date')[:3]
    # banner = BannerModel.objects.filter(active='True')
    context={
        'post' : post,
        'comments' : comments,
        'comment_form' : comment_form,
        'lposts' : lposts,
        'banners' : banner,
    }
    return render(request, 'one_post.html', context)

@login_required(login_url='/')
def add_post(request):
    """ adding new post """
    # banner = BannerModel.objects.filter(active='True')
    form = AddPostForm(request.POST or None, files=request.FILES or None)
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            form.save_m2m()
            return redirect('post_page', slug=new_post.slug)
    context = {
        'form' : form,
        'banners' : banner,
    }
    return render(request, 'add_post.html', context)

@login_required(login_url='/')
def update_post(request, slug):
    """ updating old post """
    # banner = BannerModel.objects.filter(active='True')
    post = get_object_or_404(PostModel, slug=slug, author=request.user)
    form = UpdatePostForm(request.POST or None, files=request.FILES or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('post_page', slug=post.slug)
    context = {
        'form' : form,
        'banners' : banner,
    }
    return render(request, 'update_post.html', context)

@login_required(login_url='/')
def delete_post(request, slug):
    """ deleting a post """
    # banner = BannerModel.objects.filter(active='True')
    post = get_object_or_404(PostModel, slug=slug, author=request.user).delete()
    return redirect('my_posts_page')
