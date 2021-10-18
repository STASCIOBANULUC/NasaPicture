from rest_framework import viewsets

from main.api.serializers import NasaPictureSerializers
from main.models import NasaPicture


class NasaPictureViewSet(viewsets.ModelViewSet):
    queryset = NasaPicture.objects.all()
    serializer_class = NasaPictureSerializers

