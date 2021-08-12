from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from account.forms import SignUpForm
# from blog.models import BannerModel

# banner = BannerModel.objects.filter(active='True')

@login_required(login_url='/')
def sign_out(request):
    logout(request)
    return redirect('home_url')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Yeni kullanıcı oluşturuldu.')
            return redirect('update_user_url')
        print(' ')
    else:
        form = SignUpForm()
    context={
        'form' : form
    }
    return render(request, 'sign_up.html', context)
