from django.shortcuts import render
from .models import Post



def home(request):
    postings = {
        'listings' : Post.objects.all()
    }
    return render(request, 'front/front.html',  postings)

def about(request):
    postings = {
        'listings' : Post.objects.all()
    }
    return render(request, 'front/about.html', postings )
