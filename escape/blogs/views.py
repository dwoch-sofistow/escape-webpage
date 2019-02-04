from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.

#Wszystkie wpisy na blogu
def blogmenu(request):
    blogs = Blog.objects
    return render(request, 'blogs.html', {'blogs':blogs})

#Ta funkcja kieruje na podstronę wybranego wpisu na blogu.
def blogdetail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog.html', {'blog':blog})
