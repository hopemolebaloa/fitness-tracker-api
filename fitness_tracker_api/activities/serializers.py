from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration', 'distance', 'calories', 'date', 'notes']
        read_only_fields = ['id', 'user']