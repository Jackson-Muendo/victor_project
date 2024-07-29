from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, members_list
from .views import add_member

router = DefaultRouter()
router.register(r'api/members', MemberViewSet)

urlpatterns = [
    path('', members_list, name='members_list'),
    path('', include(router.urls)),
     path('add/', add_member, name='add_member'),
]
