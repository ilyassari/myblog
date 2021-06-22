from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from blog.models import PostModel, CommentModel, BannerModel
from blog.forms import AddPostForm, UpdatePostForm, AddCommentForm

banner = BannerModel.objects.filter(active='True')
lposts =  PostModel.objects.order_by('-modified_date')[:3]

class PostView(View):
    """For screening one post page."""
    http_method_names = ['get', 'post']
    comment_form = AddCommentForm   #Parantez aç kapa olmamalı
    lposts =  PostModel.objects.order_by('-modified_date')[:3]

    def get(self, request, slug):
        post = get_object_or_404(PostModel, slug=slug)
        comments = post.p_comments.all()
        context={
            'post' : post,
            'comments' : comments,
            'comment_form' : self.comment_form,
            'lposts' : lposts,
            'banners' : banner,
        }
        return render(request, 'one_post.html', context)

    def post(self, request, slug):
        post = get_object_or_404(PostModel, slug=slug)
        comment_form = self.comment_form(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Yorum başarıyla eklendi.')
        return redirect('post_url', slug=post.slug)

# <editor-fold> *** def post
'''
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
        return redirect('post_url', slug=post.slug)
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
'''
# </editor-fold>

class AddPostView(LoginRequiredMixin, CreateView):  #LoginRequiredMixin i sola yazmak gerekiyor
    """For new post adding page"""
    http_method_names = ['get', 'post']
    login_url = reverse_lazy('sign_in_url')
    template_name = 'add_post.html'
    model = PostModel
    fields= ( 'title', 'image', 'categories', 'content')

    def get_success_url(self):
        return reverse('post_url', kwargs={
            'slug': self.object.slug
        })

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.author = self.request.user
        new_post.save()
        form.save_m2m()
        return super().form_valid(form)

# <editor-fold> ***** add_post
'''
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
            return redirect('post_url', slug=new_post.slug)
    context = {
        'form' : form,
        'banners' : banner,
    }
    return render(request, 'add_post.html', context)
'''

# </editor-fold>

class UpdatePostView(LoginRequiredMixin, UpdateView):
    """For old post updating page"""
    # http_method_names = ['get', 'post', 'put']
    login_url = reverse_lazy('sign_in_url')
    template_name = 'update_post.html'
    # model = PostModel
    fields= ( 'title', 'image', 'categories', 'content')

    def get_object(self):
        post = get_object_or_404(
            PostModel,
            slug=self.kwargs.get('slug'),
            author=self.request.user
        )
        return post

    def get_success_url(self):
        return reverse('post_url', kwargs={
            'slug': self.get_object().slug
        })

# <editor-fold> update_post
'''
@login_required(login_url='/')
def update_post(request, slug):
    """ updating old post """
    # banner = BannerModel.objects.filter(active='True')
    post = get_object_or_404(PostModel, slug=slug, author=request.user)
    form = UpdatePostForm(request.POST or None, files=request.FILES or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('post_url', slug=post.slug)
    context = {
        'form' : form,
        'banners' : banner,
    }
    return render(request, 'update_post.html', context)
'''
# </editor-fold>


class DeletePostView(LoginRequiredMixin, DeleteView):
    """docstring for DeletePostView."""
    login_url = reverse_lazy('sign_in_url')
    model = PostModel
    success_url = '/'

    def get_queryset(self):
        post_to_del = PostModel.objects.filter(slug=self.kwargs['slug'], author=self.request.user)
        return post_to_del

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# <editor-fold> delete
'''
@login_required(login_url='/')
def delete_post(request, slug):
    """ deleting a post """
    # banner = BannerModel.objects.filter(active='True')
    post = get_object_or_404(PostModel, slug=slug, author=request.user).delete()
    messages.success(request, 'Gönderi başarıyla silindi.')
    return redirect('my_posts_url')
'''
# </editor-fold>
