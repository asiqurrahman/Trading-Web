from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from PIL import Image
import requests 
from requests import get
from users.models import Profile
import zipcodes



#def home(request):

    #final_location = 10

    #postings = { 
        
        #'listings' : Post.objects.all(),
        #'final_location' : final_location
    #}
    #return render(request, 'front/front.html',  postings)


class PostListView(ListView):
    model = Post
    template_name = 'front/front.html'
    context_object_name = 'listings'
    ordering = ['-date_posted']



class SearchView(ListView):
    model = Post
    template_name = 'front/about.html'
    context_object_name = 'listings'
    ordering = ['-date_posted']

    
    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Post.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result



    
    

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
    

    #current = request.user.profile.location

    #def get_ip_address(request):
     #   x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
      #  if x_forwarded_for:
       #     ip = x_forwarded_for.split(',')[0]
        #else:
         #   ip = request.META.get('REMOTE_ADDR')
        #return ip
    
    #ip = get_ip_address(request)
    #loc_key = get('http://ipapi.co/json/?key=dhlDIr1TAg6GdxiKdfn8lVBOmEDOZlXVhPPqfIPKsmujFBXMu6')
    #loc = get('https://ipapi.co/72.76.225.203/json/')#.format(ip))    
    #address = loc.json()
    #city = address['city']
    #region = address['region']
    #area = city + ", " + region

    
       
    number_of_users2 ={
        
        'count' : x
        #'location' : area
        
    
    }

    return render(request, 'front/about.html',  number_of_users2)














def zip(request):

    check_for_zipcode = request.user.profile.location
    yap = 10

    zipcodes = {
        'check_for_zipcode' : check_for_zipcode,
         'yap' : yap
    }
    return render(request, 'front/post_form.html',  zipcodes)

