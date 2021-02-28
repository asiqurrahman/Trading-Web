from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User




def home(request):
    postings = {
        'listings' : Post.objects.all()
    }
    return render(request, 'front/front.html',  postings)

def about(request):
    
    number_of_users = User.objects.all()
    x = User.objects.count()

    
    
    number_of_users2 ={
        'car' : number_of_users,
        'count' : x
    }

    return render(request, 'front/about.html', number_of_users2)

