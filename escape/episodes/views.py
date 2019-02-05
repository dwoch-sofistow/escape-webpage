from django.shortcuts import render, get_object_or_404

from episodes.models import Episode, HiddenEpisode
from resources.models import HiddenResource

# Create your views here.
# Lista wszystkich odcinków
def episodemenu(request):
    episodes = Episode.objects
    return render(request, 'episodes.html', {'episodes':episodes})

# Podstrona odcinka wybranego z listy
def detailep(request, episode_id):
    detailepisode = get_object_or_404(Episode, pk=episode_id)
    return render(request, 'episode.html', {'episode':detailepisode})

#Strona o nas
def hiddenresource(request, hiddenresource_id):
    hidden_res = get_object_or_404(HiddenResource, pk=hiddenresource_id)
    return render(request, 'special/hiddenres.html', {'hiddenre':hidden_res})


# Schemat dla apki "Episodes"
#    home   =>  episodemenu, detailp #-1 i? -2 (wip)
#    navbar =>  episodemenu
#    episodemenu => detailp
#
