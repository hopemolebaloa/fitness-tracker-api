from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    target_hours = models.IntegerField(default=5, help_text="Weekly target in hours")
    week_start = models.DateField(default=timezone.now)