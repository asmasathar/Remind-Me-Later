from django.db import models

# Reminder model stores the details of a reminder set by the user
# Fields:
# - date: Date for the reminder
# - time: Time for the reminder
# - message: Text content of the reminder
# - reminder_type: Method of notification (e.g., SMS or Email)
# - created_at: Timestamp when the reminder was created (auto-generated)


class Reminder(models.Model):
    REMINDER_TYPE_CHOICES = [
        ('sms', 'SMS'),
        ('email', 'Email'),
    ]

    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=10, choices=REMINDER_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} ({self.reminder_type})"

