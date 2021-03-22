import requests 
from requests import get

def get_ip_address(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
        ip = get_ip_address(request)
        loc_key = get('http://ipapi.co/json/?key=dhlDIr1TAg6GdxiKdfn8lVBOmEDOZlXVhPPqfIPKsmujFBXMu6')
        loc = get('https://ipapi.co/{}/json/').format(ip)
        address = loc.json()
        city = address['city']
        region = address['region']
        area = city + ", " + region
        return area