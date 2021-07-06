from django.shortcuts import render, redirect
from django.views.generic import FormView

from blog.models import ContactModel
from blog.forms import ContactForm



class ContactView(FormView):
    """docstring for ContactView.FormView"""
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/email_sended'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) # = return redirect('self.success_url')



# <editor-fold> contact
# def contact(request):
#     banner = BannerModel.objects.filter(active='True')
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home_url')
#     context={
#         'form' : form,
#         'banners' : banner,
#     }
#     return render(request, 'contact.html', context)
# </editor-fold>
