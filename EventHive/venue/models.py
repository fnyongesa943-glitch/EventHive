from django.db import models

class Venue(models.Model):
    venue_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.venue_name