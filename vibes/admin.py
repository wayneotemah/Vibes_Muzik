from django.contrib import admin
from .models import Artist, Song


# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song)
