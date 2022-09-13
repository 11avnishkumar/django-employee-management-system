from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,help_text='Desribe yourself with 500 words only')
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='profiles/profile_avatar',default='avatar.jpg')

    def __str__(self):
        return f"Profile of {self.user}"
