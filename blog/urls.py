from django.urls import path
from blog.views import *


urlpatterns = [
    path('', home, name='home_page'),
    path('category/<slug:slug>', category, name='category_page'),
    path('post/<slug:slug>', post, name='post_page'),
    path('add_post', add_post, name='add_post_page'),
    path('update_post/<slug:slug>', update_post, name='update_post_page'),
    path('delete_post/<slug:slug>', delete_post, name='delete_post_page'),
    path('delete_comment/<int:id>', delete_comment, name='delete_comment_page'),
    path('my_posts', my_posts, name='my_posts_page'),
    path('contact', contact, name='contact_page'),
]
