from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from blog.models import PostModel, CommentModel
from section.models import BannerModel


class MyPostsView(LoginRequiredMixin, ListView):
    """docstring for CategoryModel."""
    # model = PostModel
    template_name = 'my_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        # category = get_object_or_404(CategoryModel, slug=self.kwargs['slug'])
        search = self.request.GET.get('sq')
        posts = self.request.user.a_post.order_by('-id')
        if search:
            posts = posts.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            ).distinct()
        return posts

# <editor-fold> = function based

'''
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
'''
# </editor-fold>
