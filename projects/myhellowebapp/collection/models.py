from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='books/', null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                blank=True, null=True)
