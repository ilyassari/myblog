from django import forms

from blog.models import PostModel, CommentModel

class AddCommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = (
            'content',
        )
        labels = {
            'content': 'Yorum',
        }
