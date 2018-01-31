from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status = 'published').order_by('-published')
    return render(request,'../templates/post/post_list.html',{'posts':posts})

def post_detail(request,id):
    post =get_object_or_404(Post,status = 'published' ,id=id)
    return render(request,'../templates/post/details_post.html',{'post':post})


