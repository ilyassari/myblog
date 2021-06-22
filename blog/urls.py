from django.urls import path
from django.views.generic import TemplateView, RedirectView

from blog.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home_url'),
    path('category/<slug:slug>', CategoryListView.as_view(), name='category_url'),
    path('post/<slug:slug>', PostView.as_view(), name='post_url'),
    path('add_post', AddPostView.as_view(), name='add_post_url'),
    path('update_post/<slug:slug>', UpdatePostView.as_view(), name='update_post_url'),
    path('delete_post/<slug:slug>', DeletePostView.as_view(), name='delete_post_url'),
    path('delete_comment/<int:id>', DeleteCommentView.as_view(), name='delete_comment_url'),
    path('my_posts', my_posts, name='my_posts_url'),
    path('contact', ContactView.as_view(), name='contact_url'),
]
