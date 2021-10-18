from django.db import models


class NasaPicture(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название фотографии")
    description = models.TextField(verbose_name="Описание фотографии")
    img = models.ImageField(verbose_name="Фотография", upload_to='media')
    date = models.DateField(verbose_name="Дата")

    class Meta:
        verbose_name = "Astronomy Picture of the Day"
        ordering = ("-date",)

    def __str__(self):
        return self.name
