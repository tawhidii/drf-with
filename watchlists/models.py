
from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title
