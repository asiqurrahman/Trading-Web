from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import requests 
from requests import get


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    area = "testing"
    if created:
        Profile.objects.create(user=instance, location=area)
        

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    