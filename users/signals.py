from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import requests 
from requests import get


@receiver(post_save, sender=User)
def create_profile(sender, request, instance, created, **kwargs):
    def get_ip_address(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip =  get_ip_address(request)

    loc_key = get('http://ipapi.co/json/?key=dhlDIr1TAg6GdxiKdfn8lVBOmEDOZlXVhPPqfIPKsmujFBXMu6')
    loc = get('https://ipapi.co/{}/json/'.format(ip))
    address = loc.json()
    city = address['city']
    region = address['region']
    area = city + ", " + region

    if created:
        Profile.objects.create(user=instance, location=area)
        

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    