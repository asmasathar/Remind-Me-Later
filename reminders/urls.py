from django.urls import path
from .views import create_reminder

# URL patterns for the reminders app
# Defines the endpoints accessible for creating reminders

urlpatterns = [
    path('create/', create_reminder, name='create_reminder'),
]

