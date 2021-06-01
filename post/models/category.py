from django.db import models
from autoslug import AutoSlugField

class CategoryModel(models.Model):
    """docstring for CategoryModel."""
    title = models.CharField(max_length=30, blank=False, null=False)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        text = f"id:{self.id}, title: {self.title}"
        return text
