from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class AnnouncementList(APIView):
    def get(self, request, format=None):
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = AnnouncementSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnnouncementsDetail(APIView):
    def get_object(self, pk):
        try:
            return Announcement.objects.get(id=pk)
        except Announcement.DoesNotExist:
            return Response({"Error": "This Announcement doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        serializer = AnnouncementSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        data = request.data
        serializer = AnnouncementSerializer(instance=self.get_object(pk), data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        announcement = self.get_object(pk)
        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
