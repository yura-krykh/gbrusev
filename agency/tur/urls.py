from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('city/', views.CityListView.as_view(), name='city'),
    path('city/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
    path('hotel/', views.HotelListView.as_view(), name='hotel'),
    path('hotel/<int:pk>/', views.HotelDetailView.as_view(), name='hotel_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)