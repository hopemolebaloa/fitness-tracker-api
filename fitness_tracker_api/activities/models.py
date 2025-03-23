from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('RUNNING', 'Running'),
        ('CYCLING', 'Cycling'),
        ('SWIMMING', 'Swimming'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50, choices=ACTIVITY_TYPES)
    duration = models.IntegerField(help_text="Duration in minutes")
    distance = models.FloatField(blank=True, null=True, help_text="Distance in kilometers")
    calories = models.IntegerField(blank=True, null=True, help_text="Calories burned")
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True)