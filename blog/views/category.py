from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView

from blog.models import PostModel, CategoryModel

# banner = BannerModel.objects.filter(active='True')

class CategoryListView(ListView):
    """docstring for CategoryModel."""
    # model = CategoryModel
    template_name = 'category.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        category = get_object_or_404(CategoryModel, slug=self.kwargs['slug'])
        posts = category.c_post.all().order_by('-id')
        return posts



'''
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
'''
