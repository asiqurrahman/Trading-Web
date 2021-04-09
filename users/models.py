from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
import requests
from requests import get
import zipcodes









class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(null=True, blank=True, max_length=5)
    detail_location = models.CharField(null=True, blank=True, max_length=100)
    detail_lat = models.CharField(null=True, blank=True, max_length=100)
    detail_lng = models.CharField(null=True, blank=True, max_length=100)




    def __str__(self):
        return f'{self.user.username} Profile'
    
   




    




    
