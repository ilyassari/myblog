import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import DeleteView
from django.urls import reverse, reverse_lazy

from blog.models import CommentModel


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    """docstring for DeleteCommentView."""
    login_url = reverse_lazy('sign_in_url')
    model = CommentModel
    pk_url_kwarg = 'id'
    success_message = "Comment was deleted successfully."

    def get_queryset(self):
        comment_to_del = CommentModel.objects.filter(id=self.kwargs['id'], author=self.request.user)
        if self.request.user.is_authenticated:
            logger = logging.getLogger('comment_deleted')
            logger.info(f'post-slug: {comment_to_del[0].post.slug}, user: {self.request.user.username}')
        return comment_to_del

    def get(self, request, *args, **kwargs):
        # return self.post(request, *args, **kwargs)
        return self.post(request, *args, **kwargs )

    def get_success_url(self):
        return reverse('post_url', kwargs={
            'slug': self.object.post.slug
        })

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteCommentView, self).delete(request, *args, **kwargs)



# <editor-fold> delete
'''
@login_required(login_url='/')
def delete_comment(request, id):
    """ deleting a comment """
    # banner = BannerModel.objects.filter(active='True')
    comment = get_object_or_404(CommentModel, id=id, )
    if comment.author == request.user or comment.post.author == request.user:
        comment.delete()
        messages.success(request, 'Yorum başarıyla silindi.')
        return redirect('post_url', slug=comment.post.slug)
    return redirect('home_url')
'''

# </editor-fold>
