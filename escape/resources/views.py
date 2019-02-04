from django.shortcuts import render, get_object_or_404

from resources.models import Resource, HiddenResource

# Create your views here.
#Wszystkie epizody w skrócie
def resourcemenu(request):
    episodes = Resource.objects
    return render(request, 'resources/resourcemenu.html', {'resources':resources})

#Ta funkcja kieruje na podstronę wybranego epizodu
def detailres(request, Resource_id):
    detailresource = get_object_or_404(Resource, pk=Resource_id)
    return render(request, 'resources/details.html', {'resource':detailresource})

#Strona o nas
def hiddenresource(request, HideenResource_id):
    hidden_res = get_object_or_404(HiddenResource, pk=HiddenResource_id)
    return render(request, 'resources/hiddenep.html', {'hidden':hidden_ep})
