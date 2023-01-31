from rest_framework import serializers
from .models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'owner', 'status', 'title', 'description', 'price', 'is_active', 'view_count']
