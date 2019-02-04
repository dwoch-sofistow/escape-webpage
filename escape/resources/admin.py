from django.contrib import admin

from .models import Resource, HiddenResource
# Register your models here.
admin.site.register(Resource)
admin.site.register(HiddenResource)
