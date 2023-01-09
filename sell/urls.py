from django.urls import path
from .views import AnnouncementList, AnnouncementsDetail

urlpatterns = [
    path('', AnnouncementList.as_view()),
    path('<int:pk>/', AnnouncementsDetail.as_view())
]
