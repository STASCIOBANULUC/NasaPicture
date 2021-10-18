import os

from django.core.files.base import ContentFile
from django.core.management import BaseCommand
import requests
from django.db.models import Model

from main.models import NasaPicture


class Command(BaseCommand):
    help = 'Extract API'

    def handle(self, *args, **options):
        url = 'https://api.nasa.gov/planetary/apod?api_key=6t0vUMnVuZmzxUIoSWMfhIMz2KUivOujCokmMeD6'
        response = requests.get(url)
        data = response.json()
        link = data["hdurl"]
        r = requests.get(link)
        obj = NasaPicture.objects.create(name=data["title"], description=data["explanation"], date=data["date"])
        if r.ok:
            obj.img.save(os.path.basename(link), ContentFile(r.content))
