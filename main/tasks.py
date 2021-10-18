import os

import requests
from celery import shared_task
from django.core.files.base import ContentFile

from .models import NasaPicture


@shared_task
def create_new_model():
    url = 'https://api.nasa.gov/planetary/apod?api_key=6t0vUMnVuZmzxUIoSWMfhIMz2KUivOujCokmMeD6'
    response = requests.get(url)
    data = response.json()
    link = data["hdurl"]
    r = requests.get(link)
    obj = NasaPicture.objects.create(name=data["title"], description=data["explanation"], date=data["date"])
    if r.ok:
        obj.img.save(os.path.basename(link), ContentFile(r.content))
    return obj.name



