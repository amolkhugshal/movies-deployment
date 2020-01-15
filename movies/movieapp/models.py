from django.db import models

# Create your models here.
class Movielist(models.Model):
    poster = models.ImageField(upload_to='movie_poster')
    title = models.TextField()
    download_link = models.URLField()

    def __str__(self):
        return str(self.title)
