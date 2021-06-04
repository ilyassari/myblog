from django.urls import path
from blog.views import *


urlpatterns = [
    path('', home, name='home_page'),
    path('contact', contact, name='contact_page'),
    path('post/<slug:slug>', post, name='post_page'),
    path('category/<slug:slug>', category, name='category_page'),
]
