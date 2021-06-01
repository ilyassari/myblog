from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

from post.models import CategoryModel
from ckeditor.fields import RichTextField


def image_path(instance, imagename): # uuid4().hex + ext
    dir_path = 'post/images/'
    # name = str(self.unique_name)
    name = uuid.uuid4().hex
    extension = '.'+str(instance.upload).split('.')[-1]
    return os.path.join(dir_path, name+extension)

class PostModel(models.Model):
    """docstring for PostModel."""
    title = models.CharField(max_length=30, blank=False, null=False)
    images = models.ImageField(upload_to=image_path)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_post')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='c_post')
    content = RichTextField()

    def __str__(self):
        text = f"id:{self.id}, title: {self.title}"
        return text