from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from PIL import Image
import requests 
from requests import get
from users.models import Profile




def home(request):

    postings = {
        'listings' : Post.objects.all()
    }
    return render(request, 'front/front.html',  postings)


class PostListView(ListView):
    model = Post
    template_name = 'front/front.html'
    context_object_name = 'listings'
    ordering = ['-date_posted']
    

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'post_image', 'title2', 'content2', 'post_image2']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    













def about(request):
    
    x = User.objects.count()
    loc = get('http://ipapi.co/json/?key=dhlDIr1TAg6GdxiKdfn8lVBOmEDOZlXVhPPqfIPKsmujFBXMu6')

    current = request.user.profile.location

            


    number_of_users2 ={
        
        'count' : x,
        'location' : current
        
    
    }

    return render(request, 'front/about.html', number_of_users2)

