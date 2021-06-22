from django.urls import path
from django.contrib.auth.views import LoginView

from account.views import *


urlpatterns = [
    path('sign_up', sign_up, name='sign_up_url'),
    path('sign_in', LoginView.as_view(
        template_name = 'sign_in.html'
    ), name='sign_in_url'),
    path('update_user', update_user, name='update_user_url'),
    path('change_pwd', change_pwd, name='change_pwd_url'),
    path('sign_out', sign_out, name='sign_out_url'),
    path('profile/<str:username>', UserDetailView.as_view(), name='profile_url'),

]
