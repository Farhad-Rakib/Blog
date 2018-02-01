from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

# Create your views here.

def post_list(request):
    posts_list = Post.objects.filter(status = 'published').order_by('-published')
    paginator = Paginator(posts_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request,'../templates/post/post_list.html',{'posts':posts})

def post_detail(request,id):
    post =get_object_or_404(Post,status = 'published' ,id=id)
    return render(request,'../templates/post/details_post.html',{'post':post})


