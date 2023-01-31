from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework.response import Response
from rest_framework import status, filters, generics
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly


class AnnouncementListAPIView(generics.ListCreateAPIView):
    """
    List all Announcements, or create a new Announcement.
    """
    permission_classes = [IsOwnerOrReadOnly]
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)
    queryset = Announcement.objects.filter(status='A')
    serializer_class = AnnouncementSerializer


class AnnouncementsDetail(APIView):
    """
    Retrieve, update or delete a Announcement instance.
    """
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Announcement.objects.get(id=pk)
        except Announcement.DoesNotExist:
            return Response({"Error": "This Announcement doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        serializer = AnnouncementSerializer(self.get_object(pk))
        obj = self.get_object(pk)
        obj.view_count = obj.view_count + 1
        obj.save()
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
