from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Announcement(models.Model):
    STATUS_ACCEPTED = 'A'
    STATUS_PENDING = 'P'
    STATUS_REJECTED = 'R'

    STATUS_CHOICES = (
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_PENDING, "Pending"),
        (STATUS_REJECTED, "Rejected")
    )
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='announcement', default='1')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.id})"
