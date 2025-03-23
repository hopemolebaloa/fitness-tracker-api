from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Goal
        fields = ['id', 'user', 'target_hours', 'week_start']
        read_only_fields = ['id', 'user']