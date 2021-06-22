from django import forms

from blog.models import PostModel

class AddPostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = (
            'title', 'categories', 'image', 'content',
        )
        # labels = {
        #     'title': 'Başlık',
        #     'categories': 'Kategoriler',
        #     'image': 'Görsel',
        #     'content': 'İçerik',
        # }


class UpdatePostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = (
            'title', 'categories', 'image', 'content',
        )
        # labels = {
        #     'title': 'Başlık',
        #     'categories': 'Kategoriler',
        #     'image': 'Görsel',
        #     'content': 'İçerik',
        # }
