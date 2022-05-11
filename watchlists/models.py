
from django.db import models

# Create your models here.
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
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Watchlists'

    def __str__(self):
        return self.title + ' ' + str(self.created)
