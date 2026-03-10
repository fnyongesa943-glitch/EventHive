from django.db import models
from user.models import User
from event.models import Event

class booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tickets_booked = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.event.event_name}"