from django.db import models
from django.db import models
from orginizer.models import Orginizer
from venue.models import Venue

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    orginizer = models.ForeignKey(Orginizer, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    event_date = models.DateField()
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    available_tickets = models.IntegerField()

    def __str__(self):
        return self.event_name

