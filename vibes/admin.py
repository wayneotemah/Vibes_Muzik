from django.contrib import admin
from .models import Artist, Song


# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class SongAdmin(admin.ModelAdmin):
    search_fields = ["song_title"]
    list_filter = ["song_genre"]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
