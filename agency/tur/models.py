from django.conf import settings
from django.db import models
from django.urls import reverse
# from django.contrib.auth import get_user_model
# User=get_user_model()

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    photo = models.ImageField(upload_to='img/city/', verbose_name='Фото')
    body = models.TextField(max_length=200, verbose_name='Описание')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор', null=False)

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
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotelName = models.ForeignKey(
        hotel,
        on_delete=models.CASCADE,
        related_name="tour",
    )

    def get_absolute_url(self):
        return reverse("tour_detail", args=[str(self.id)])

    def __str__(self):
        return self.name