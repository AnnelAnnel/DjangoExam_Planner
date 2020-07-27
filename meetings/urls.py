from django.urls import path
from . import views

urlpatterns = [
    path('', views.meetings_list, name='meetings_list'),
    path('create', views.create_meeting, name='create_meeting'),
    path('<int:id>', views.meetings_detail, name='meetings_detail'),
    path('rooms', views.rooms_list, name='rooms_list'),
]