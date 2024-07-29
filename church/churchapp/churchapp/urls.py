from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet
from members.views import MemberViewSet
from .views import index

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'members', MemberViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('events/', include('events.urls')),
    path('members/', include('members.urls')),
]
