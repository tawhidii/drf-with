
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from django.contrib.auth.models import User



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



class Review(models.Model):
    review_user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=250)
    watchlist = models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='review')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + '---' + self.watchlist.title
    