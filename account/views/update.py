from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from account.forms import UpdateUserForm
from blog.models import BannerModel

banner = BannerModel.objects.filter(active='True')

@login_required(login_url='/')
def update_user(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil Güncellendi.')
            return redirect('update_user_url')
    else:
        form = UpdateUserForm(instance = request.user)
    context={
        'banners' : banner,
        'form' : form
    }
    return render(request, 'update_user.html', context)

@login_required(login_url='/')
def change_pwd(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifre başarıyla değiştirildi.')
            return redirect('change_pwd_url')
    else:
        form = PasswordChangeForm(request.user)

    context={
        'banners' : banner,
        'form' : form
    }
    return render(request, 'change_pwd.html', context)
