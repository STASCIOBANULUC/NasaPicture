from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import NasaPicture


class MainView(ListView):
    queryset = NasaPicture.objects.all().order_by('-date')
    template_name = "index.html"
    context_object_name = "photos"
    paginate_by = 14


class NasaPictureDetail(DetailView):
    template_name = 'photo-detail.html'
    model = NasaPicture
    context_object_name = 'photo'

