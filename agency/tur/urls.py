from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .models import City, hotel, tour

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('city/', views.CityListView.as_view(), name='city'),
    path('city/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
    path('city/new/', views.CityCreateView.as_view(), name='city_new'),
    path('city/delete/<int:pk>', views.CityDeleteView.as_view(), name='city_delete'),
    path('city/edit/<int:pk>', views.CityUpdateView.as_view(), name='city_edit'),
    path('city/list/', views.DataListView.as_view(model = City), name='list_city'),
    path('hotel/', views.HotelListView.as_view(), name='hotel'),
    path('hotel/<int:pk>/', views.HotelDetailView.as_view(), name='hotel_detail'),
    path("hotel/new/", views.HotelCreateView.as_view(), name="hotel_new"),
    path('hotel/list/', views.DataListView.as_view(model = tour), name='list_tour'),
    path('tour/', views.TourListView.as_view(), name='tour'),
    path('tour/action/', views.TourActionListView.as_view(), name='acton'),
    path('tour/<int:pk>/', views.TourDetailView.as_view(), name='tour_detail'),
    path('tour/new', views.TourCreateView.as_view(), name='tour_new'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)