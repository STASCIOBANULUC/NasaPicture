from django.urls import path, include
from rest_framework import routers

from main.api.views import NasaPictureViewSet

router = routers.DefaultRouter()
router.register(r'photo', NasaPictureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
