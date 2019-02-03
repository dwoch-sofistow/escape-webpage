from django.shortcuts import render, get_object_or_404

from .models import Blog

def blogmenu(request):
    blogs = Blog.objects
    return render(request, 'blog/blogmenu.html', {'blogs':blogs})

#Ta funkcja kieruje na podstronę wybranego wpisu na blogu.
def details(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog':detailblog})
# Create your views here.
