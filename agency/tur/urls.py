from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('city/', views.CityListView.as_view(), name='city'),
    path('city/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
    path('city/new/', views.CityCreateView.as_view(), name='city_new'),
    path('city/delete/<int:pk>', views.CityDeleteView.as_view(), name='city_delete'),
    path('city/edit/<int:pk>', views.CityUpdateView.as_view(), name='city_edit'),
    path('city/list/', views.CityDataListView.as_view(), name='list_city'),

    path('hotel/', views.HotelListView.as_view(), name='hotel'),
    path('hotel/<int:pk>/', views.HotelDetailView.as_view(), name='hotel_detail'),
    path('hotel/new/', views.HotelCreateView.as_view(), name='hotel_new'),
    path('hotel/edit/<int:pk>', views.HotelUpdateView.as_view(), name='hotel_edit'),
    path('hotel/delete/<int:pk>', views.HotelDeleteView.as_view(), name='hotel_delete'),
    path('hotel/list/', views.HotelDataListView.as_view(), name='list_hotel'),

    path('tour/list/', views.TourDataListView.as_view(), name='list_tour'),
    path('tour/', views.TourListView.as_view(), name='tour'),
    path('tour/action/', views.TourActionListView.as_view(), name='acton'),
    path('tour/<int:pk>/', views.TourDetailView.as_view(), name='tour_detail'),
    path('tour/new', views.TourCreateView.as_view(), name='tour_new'),
    path('tour/edit/<int:pk>', views.TourUpdateView.as_view(), name='tour_edit'),
    path('tour/delete/<int:pk>', views.TourDeleteView.as_view(), name='tour_delete'),
    path('tour/<int:pk>/buy', views.TourBuyView.as_view(), name='tour_buy'),
    path('tour/purchased', views.TourBuyListView.as_view(), name='tour_purchased'),

    path("food/add", views.FoodCreateVies.as_view(), name="food_new"),
    path("food/list", views.FoodTableView.as_view(), name="list_food"),
    path("food/delete/<int:pk>", views.FoodDeleteView.as_view(), name="food_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)