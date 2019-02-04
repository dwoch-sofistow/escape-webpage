from django.shortcuts import render, get_object_or_404

from . import urls

from .models import Blog
from episodes.models import Episode, HiddenEpisode
from resources.models import Resource

# Create your views here.
#Strona Główna
def home(request):
    blogs = Blog.objects
    episodes = Episode.objects
    resources = Resource.objects
    return render(request, 'home.html', {'blogs':blogs,'episodes':episodes,'resources':resources})
#Wszystkie wpisy na blogu
def blogmenu(request):
    blogs = Blog.objects
    return render(request, 'blog/blogmenu.html', {'blogs':blogs})

#Ta funkcja kieruje na podstronę wybranego wpisu na blogu.
def details(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog':detailblog})
#Strona o nas
def about(request):
    episodes_h = HiddenEpisode.objects
    return render(request, 'about.html', {'episodes':episodes_h})
