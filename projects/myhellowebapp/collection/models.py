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


# class MyRegistrationView(RegistrationView):
#     def get_success_url(self, request, user):
#         # the named URL that we want to redirect to after
#         # successful registration
#         return ('registration_create_bookuser')
