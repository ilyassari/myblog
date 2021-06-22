from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView

from blog.models import PostModel, CommentModel, BannerModel

class HomeView(ListView):
    """docstring for CategoryModel."""
    # model = PostModel
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        # category = get_object_or_404(CategoryModel, slug=self.kwargs['slug'])
        search = self.request.GET.get('sq')
        posts = PostModel.objects.order_by('-id')
        if search:
            posts = posts.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            ).distinct()
        return posts

# <editor-fold>

'''
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
'''
# </editor-fold>
