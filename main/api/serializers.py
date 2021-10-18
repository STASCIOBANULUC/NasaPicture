from rest_framework import serializers

from main.models import NasaPicture


class NasaPictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = NasaPicture
        fields = ['id', 'name', 'description', 'date', ]

