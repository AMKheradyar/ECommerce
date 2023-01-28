from django.urls import path
from .views import AnnouncementListAPIView, AnnouncementsDetail

urlpatterns = [
    path('', AnnouncementListAPIView.as_view()),
    path('<int:pk>/', AnnouncementsDetail.as_view())
]
