from django.shortcuts import render, get_object_or_404

from episodes.models import Episode, HiddenEpisode

# Create your views here.
#Wszystkie epizody w skrócie
def episodemenu(request):
    episodes = Episode.objects
    return render(request, 'episodes/episodemenu.html', {'episodes':episodes})

#Ta funkcja kieruje na podstronę wybranego epizodu
def detailep(request, Episode_id):
    detailepisode = get_object_or_404(Episode, pk=Episode_id)
    return render(request, 'episodes/episode.html', {'episode':detailepisode})

#Strona o nas
def hiddenepisode(request, HideenEpisode_id):
    hidden_ep = get_object_or_404(HiddenEpisode, pk=HiddenEpisode_id)
    return render(request, 'episode/hiddenep.html', {'hidden':hidden_ep})
