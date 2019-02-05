from django.shortcuts import render, get_object_or_404

from resources.models import Resource

# Create your views here.
#Wszystkie epizody w skrócie
def resourcemenu(request):
    resources = Resource.objects
    return render(request, 'resources.html', {'resources':resources})

#Ta funkcja kieruje na podstronę wybranego epizodu
def detailres(request, Resource_id):
    detailresource = get_object_or_404(Resource, pk=Resource_id)
    return render(request, 'resource.html', {'resource':detailresource})
