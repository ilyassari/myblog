from django.db import models
# from django.contrib.auth.models import User

from account.models import CustomUserModel as User
from post.models import PostModel

class CommentModel(models.Model):
    """docstring for CommentModel."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_comments')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='p_comments')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        text = f"id:{self.id}, post: {self.post}"
        return text
