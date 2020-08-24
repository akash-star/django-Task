from django.db import models

# Create your models here.
class Scheduler(models.Model):
    url_for_site = models.URLField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.url_for_site
        