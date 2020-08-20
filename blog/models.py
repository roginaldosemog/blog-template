from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__ (self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__ (self):
        return self.title