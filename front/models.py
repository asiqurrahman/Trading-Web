from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import zipcodes



class Post(models.Model):
    title = models.CharField(max_length=100)
    title2 = models.CharField( max_length=100)
    content = models.TextField(default=timezone.now)
    content2 = models.TextField(default=timezone.now)
    post_image = models.ImageField(upload_to='post_pics')
    post_image2 = models.ImageField(upload_to='post2_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
    
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



           