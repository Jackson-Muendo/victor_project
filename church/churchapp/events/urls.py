from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, events_list
from .views import add_event

router = DefaultRouter()
router.register(r'api/events', EventViewSet)

urlpatterns = [
    path('', events_list, name='events_list'),
    path('', include(router.urls)),
     path('add/', add_event, name='add_event'),
]
