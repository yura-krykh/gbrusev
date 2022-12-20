from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import City, hotel, tour, food
from django.urls import reverse_lazy
from django.conf import settings
from .forms import *

user = settings.AUTH_USER_MODEL

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

class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    template_name = 'city\city_new.html'
    fields = ['name', 'photo', 'body', ]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CityUpdateView(LoginRequiredMixin, UpdateView):
    model = City
    fields = '__all__'
    template_name = 'city\city_edit.html'
    success_url = reverse_lazy('list_city')
    login_url = 'login'

class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'city\city_delete.html'
    success_url = reverse_lazy('list_city')
    login_url = 'login'

class CityDataListView(ListView):
    model = City
    fields = '__all__'
    template_name = 'city\city_table.html'

class TourDataListView(ListView):
    model = tour
    fields = '__all__'
    template_name = 'tour\\tour_table.html'

class HotelListView(ListView):
    model = City
    template_name = 'hotel\hotel.html'

class HotelDetailView(DetailView):
    model = hotel
    template_name = 'hotel\hotel_detail.html'

class HotelCreateView(LoginRequiredMixin, CreateView):
    model = hotel
    template_name = 'city\city_new.html'
    fields = ['name', 'photo', 'body', 'cityName', ]
    success_url = reverse_lazy('list_hotel')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(HotelCreateView, self).form_valid(form)

class HotelUpdateView(LoginRequiredMixin, UpdateView):
    model = hotel
    fields = '__all__'
    template_name = 'city\city_edit.html'
    success_url = reverse_lazy('list_hotel')
    login_url = 'login'

class HotelDeleteView(LoginRequiredMixin, DeleteView):
    model = hotel
    template_name = 'city\city_delete.html'
    success_url = reverse_lazy('list_hotel')
    login_url = 'login'

class HotelDataListView(ListView):
    model = hotel
    fields = '__all__'
    template_name = 'hotel\hotel_table.html'

class TourListView(ListView):
    model = tour
    template_name = "tour\\tour.html"

class TourActionListView(ListView):
    model = tour
    template_name = "tour\\tour.html"

    def get_queryset(self):
        action = tour.objects.filter(event = True)
        action = tour.objects.filter(purchase = False)
        return action

class TourDetailView(DetailView):
    model = tour
    template_name = 'tour\\tour_detail.html'

class TourCreateView(LoginRequiredMixin, CreateView):
    model = tour
    template_name = 'city\city_new.html'
    fields = ['name', 'body', 'event', 'cost', 'hotelName', ]
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TourCreateView, self).form_valid(form)

class TourUpdateView(LoginRequiredMixin, UpdateView):
    model = tour
    fields = '__all__'
    template_name = 'city\city_edit.html'
    success_url = reverse_lazy('list_tour')
    login_url = 'login'

class TourDeleteView(LoginRequiredMixin, DeleteView):
    model = tour
    template_name = 'city\city_delete.html'
    success_url = reverse_lazy('list_tour')
    login_url = 'login'

class TourBuyView(LoginRequiredMixin, UpdateView):
    model = tour
    template_name = 'tour\\buy.html'
    fields = ['foodName',]
    login_url = 'login'

    def form_valid(self, form):
        # instance = form.save(commit=False)
        form.instance.action = False
        form.instance.purchase = True
        form.instance.buying = self.request.user
        return super(TourBuyView, self).form_valid(form)

    # def approve_group(request, pk, form):
    #     instance = form.save(commit=False)
    #     instance.purchase = True
    #     return redirect(request, 'home')

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

# def TourBuyView(form, pk):
#     instance = form.save(commit=False)
#     instance.purchase = True
#     return redirect('home')

class TourBuyListView(ListView):
    model = tour
    fields = '__all__'
    template_name = 'tour\\tour_table.html'

    def get_queryset(self):
        buying = tour.objects.filter(purchase = True)
        buying = tour.objects.filter(buying = self.request.user)
        return buying

    # def get_queryset(self):
    #     action = tour.objects.filter(event = True)
    #     action = tour.objects.filter(purchase = False)
    #     return action

class FoodCreateVies(LoginRequiredMixin, CreateView):
    model = food
    template_name = 'city\city_new.html'
    fields = ('name', )
    success_url = reverse_lazy('list_food')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(FoodCreateVies, self).form_valid(form)


class FoodTableView(ListView):
    model = food
    fields = '__all__'
    template_name = 'food\\food_table.html'

class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = tour
    template_name = 'city\city_delete.html'
    success_url = reverse_lazy('list_food')
    login_url = 'login'