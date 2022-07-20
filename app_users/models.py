from django.contrib.auth.models import User
from django.db import models

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=20, blank=True)
    photo_profile = models.ImageField(upload_to='avatars/')

    class Meta:
        db_table = 'db_profile'
