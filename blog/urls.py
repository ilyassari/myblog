from django.urls import path
from blog.views import *


urlpatterns = [
    path('', home, name='home_page'),
]
