from django.shortcuts import render, get_object_or_404

from episodes.models import Episode, HiddenEpisode

# Create your views here.
#Wszystkie epizody w skrócie
def episodemenu(request):
    episodes = Episode.objects
    return render(request, 'episodes.html', {'episodes':episodes})

#Ta funkcja kieruje na podstronę wybranego epizodu
def detailep(request, episode_id):
    detailepisode = get_object_or_404(Episode, pk=episode_id)
    return render(request, 'episode.html', {'episode':detailepisode})

#Strona o nas
def hiddenepisode(request, hiddenepisode_id):
    hidden_ep = get_object_or_404(HiddenEpisode, pk=hiddenepisode_id)
    return render(request, 'special/hidden.html', {'hidden':hidden_ep})
