from django.urls import path
from django.contrib.auth.views import LoginView

from account.views import *


urlpatterns = [
    path('sign_up', sign_up, name='sign_up_page'),
    path('sign_in', LoginView.as_view(
        template_name = 'sign_in.html'
    ), name='sign_in_page'),
    path('update_user', update_user, name='update_user_page'),
    path('change_pwd', change_pwd, name='change_pwd_page'),
    path('sign_out', sign_out, name='sign_out_page'),
]
