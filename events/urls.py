
from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('events/', views.event_list, name='event_list'),
    path('events/add/', views.event_create, name='event_add'),
]
