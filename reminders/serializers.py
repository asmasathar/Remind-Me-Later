from rest_framework import serializers
from .models import Reminder

# Serializer to convert reminder model instances to JSON and validate input data
# Uses ModelSerializer for automatic field mapping

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
