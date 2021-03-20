from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
import requests 
from requests import get

class Profile(models.Model):
    loc = get('http://ipapi.co/json/?key=dhlDIr1TAg6GdxiKdfn8lVBOmEDOZlXVhPPqfIPKsmujFBXMu6')
    address = loc.json()
    city = address['city']
    region = address['region']
    area = city + ", " + region
        

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=100, default=area)
    

    def __str__(self):
        return f'{self.user.username} Profile'



def save(self, *args, **kwargs):
    super().save(*args, **kwargs)  # saving image first

    img = Image.open(self.image.path) # Open image using self

    if img.height > 300 or img.width > 300:
        new_img = (300, 300)
        img.thumbnail(new_img)
        img.save(self.image.path)
