from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):

    posts = Post.objects.filter(status = 'published')
    return render(request,'../templates/post/post_list.html',{'posts':posts})

