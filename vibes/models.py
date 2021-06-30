from django.db import models
from PIL import Image


# Create your models here.
class Artist(models.Model):
    # class for artists
    name = models.CharField(max_length=200)
    artistic_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    description = models.TextField(max_length=1000)
    profile = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')

    def save(self):
        """
        function to save and resize the profile piz to a 900x900 ratio
        save the file then edit and overwrite saves file
        """
        super(Artist, self).save()
        img = Image.open(self.profile.path)
        if img.height > 900 and img.width > 900:
            output_size = (900, 900)
            img.thumbnail(output_size)
            img.save(self.profile.path)

    def __str__(self):
        return f'{self.artistic_name} , r_name: {self.name}'


class Song(models.Model):
    # class for songs related to artist
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    release_date = models.DateField()
    song_genre = models.CharField(max_length=50)
    # art_work = models.ImageField(upload_to='art_works')
    song_file = models.FileField(upload_to='music')

    # def save(self):
    #     """
    #     function to save and resize the profile piz to a 900x900 ratio
    #     save the file then edit and overwrite saves file

    # uncomment after version improvement
    #     """
    #
    #     super(Song, self).save()
    #
    #     img = Image.open(self.art_work.path)
    #     if img.height > 300 and img.width > 300:
    #         output_size = (100, 100)
    #         img.thumbnail(output_size)
    #         img.save(self.art_work.path)

    def __str__(self):
        return f'{self.artist.artistic_name},{self.song_title}'
