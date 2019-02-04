from django.shortcuts import render, get_object_or_404

from blogs.models import Blog
from episodes.models import Episode, HiddenEpisode
from resources.models import Resource

#Strona Główna
def home(request):
    blogs = Blog.objects
    episodes = Episode.objects
    resources = Resource.objects
    return render(request, 'home.html', {'blogs':blogs,'episodes':episodes,'resources':resources})

#Strona o nas
def about(request):
    episodes_h = HiddenEpisode.objects
    return render(request, 'about.html', {'episodes':episodes_h})
