from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
import requests
from requests import get
from .utils import get_ip_address




class Profile(models.Model):
    
    area = "placeholder"
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=100, default=area)



    def __str__(self):
        return f'{self.user.username} Profile'
    
    




    
