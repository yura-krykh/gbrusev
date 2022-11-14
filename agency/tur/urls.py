from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('city/', views.CityListView.as_view(), name='city'),
    path('city/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
    path('city/new/', views.CityCreateView.as_view(), name='city_new'),
    path('hotel/', views.HotelListView.as_view(), name='hotel'),
    path('hotel/<int:pk>/', views.HotelDetailView.as_view(), name='hotel_detail'),
    path("hotel/new/", views.HotelCreateView.as_view(), name="hotel_new"),
    path('tour/', views.TourListView.as_view(), name='tour'),
    path('tour/action/', views.TourActionListView.as_view(), name='acton'),
    path('tour/<int:pk>/', views.TourDetailView.as_view(), name='tour_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)