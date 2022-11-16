from django.db import models
from django.urls import reverse

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    photo = models.ImageField(upload_to='img/city/', verbose_name='Фото')
    body = models.TextField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("city_detail", args=[str(self.id)])

    def get_hotels(self):
        return self.hotel.all()

    # def meta(self):
    #     return fields


class hotel(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='img/hotel/')
    body = models.TextField(max_length=200)
    cityName = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="hotel",
    )

    def get_absolute_url(self):
        return reverse("hotel_detail", args=[str(self.id)])

    def __str__(self):
        return self.name

class tour(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='img/tour/')
    body = models.TextField(max_length=200)
    event = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    hotelName = models.ForeignKey(
        hotel,
        on_delete=models.CASCADE,
        related_name="tour",
    )

    def get_absolute_url(self):
        return reverse("tour_detail", args=[str(self.id)])

    def __str__(self):
        return self.name