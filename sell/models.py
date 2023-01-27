from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Announcement(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='announcement', default='1')
    STATUS_STATES = (
        ('A', "Accepted"),
        ('P', "Pending"),
        ('R', "Rejected")
    )
    status = models.CharField(max_length=1, choices=STATUS_STATES, default='P')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.id})"
