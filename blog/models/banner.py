import uuid
import os

from django.db import models


def image_path(instance, imagename): # uuid4().hex + ext
    dir_path = 'blog/images/'
    # name = str(self.unique_name)
    name = uuid.uuid4().hex
    extension = '.'+str(instance.image).split('.')[-1]
    return os.path.join(dir_path, name+extension)

class BannerModel(models.Model):
    """docstring for BannerModel."""
    title = models.CharField(max_length=30, blank=False, null=False)
    image = models.ImageField(upload_to=image_path)
    link = models.CharField(max_length=260, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        text = f"id:{self.id}, title: {self.title}"
        return text
