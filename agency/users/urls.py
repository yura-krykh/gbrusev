from django.urls import path
from . import views
  
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('logout/', views.logout_user, name='logout')
]