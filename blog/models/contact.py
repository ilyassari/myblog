from django.db import models

class ContactModel(models.Model):
    """docstring for ContactModel.models.Model"""
    title = models.CharField(max_length=30)
    email = models.EmailField(max_length=250)
    full_name = models.CharField(max_length=150)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        text = f"id:{self.id}, title: {self.title}"
        return text
