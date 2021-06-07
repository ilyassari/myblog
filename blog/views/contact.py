from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from blog.models import ContactModel, BannerModel
from blog.forms import ContactForm


def contact(request):
    banner = BannerModel.objects.filter(active='True')
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    context={
        'form' : form,
        'banners' : banner,
    }
    return render(request, 'contact.html', context)
