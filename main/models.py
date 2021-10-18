from django.db import models
from django.urls import reverse


class NasaPicture(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название фотографии")
    description = models.TextField(verbose_name="Описание фотографии")
    img = models.ImageField(verbose_name="Фотография", upload_to='photo/%Y/%m/%d/')
    date = models.DateField(verbose_name="Дата")

    class Meta:
        verbose_name = "Astronomy Picture of the Day"
        ordering = ("-date",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo-detail', kwargs={'pk': self.pk})
