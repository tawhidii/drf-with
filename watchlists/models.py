

from django.db import models

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name




class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.TextField()
    is_active = models.BooleanField(default=True)
    platform = models.ForeignKey(StreamingPlatform,on_delete=models.CASCADE,related_name='watchlist')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Watchlists'

    def __str__(self):
        return self.title + ' ' + str(self.created)
