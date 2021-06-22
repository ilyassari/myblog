from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from account.models import CustomUserModel

class UserDetailView(DetailView):
    """docstring for UserDetailView."""
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(
            CustomUserModel, username=self.kwargs.get('username')
        )
