from django.shortcuts import render, get_object_or_404

from .models import Blog
from episodes.models import HiddenEpisode
from resources.models import HiddenResource

# Create your views here.

#Wszystkie wpisy na blogu
def blogmenu(request):
    blogs = Blog.objects
    return render(request, 'blogs.html', {'blogs':blogs})

#Ta funkcja kieruje na podstronę wybranego wpisu na blogu.
def blogdetail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog.html', {'blog':blog})

#Ukryte epizody
def hiddenepisode(request, hiddenepisode_id):
    hidden_ep = get_object_or_404(HiddenEpisode, pk=hiddenepisode_id)
    hidden_re = get_object_or_404(HiddenResource, pk=hiddenresource_id)
    return render(request, 'special/hiddeneps.html', {'hidden':hidden_ep, 'resource':hidden_re})

#def hiddenres(request, hiddenresource_id):
#    hidden_re = get_object_or_404(HiddenResource, pk=hiddenresource_id)
#    return render(request, 'special/hiddeneps.html', {'resource':hidden_re})
