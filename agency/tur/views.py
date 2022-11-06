from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import City, hotel, tour

class HomePageView(ListView):
    model = City
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['hotel'] = hotel.objects.all()
        return context

class CityListView(ListView):
    model = City
    template_name = 'city\city.html'

class CityDetailView(DetailView):
    model = City
    template_name = 'city\city_detail.html'

class HotelListView(ListView):
    model = City
    template_name = 'hotel\hotel.html'

class HotelDetailView(DetailView):
    model = hotel
    template_name = 'hotel\hotel_detail.html'

class TourListView(ListView):
    model = tour
    template_name = "tour\\tour.html"

class TourActionListView(ListView):
    model = tour
    template_name = "tour\\tour.html"

    def get_queryset(self):
        actions = tour.objects.filter(event = True)
        return actions

class TourDetailView(DetailView):
    model = tour
    template_name = 'tour\\tour_detail.html'