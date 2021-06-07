from django import forms

from blog.models import ContactModel

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = (
            'email', 'full_name', 'message',
        )
        labels = {
            'email': 'E-posta : ',
            'full_name': 'İsim Soyisim : ',
            'message': 'Mesajınız : ',

        }
