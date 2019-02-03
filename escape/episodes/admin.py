from django.contrib import admin

# Register your models here.
from .models import Episode, HiddenEpisode
# Register your models here.
admin.site.register(Episode)
admin.site.register(HiddenEpisode)
