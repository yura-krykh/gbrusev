from django.urls import path
from . import views
  
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('signup/', views.RegisterUser.as_view(), name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('password-change/done/', views.ChangePasswordDoneView.as_view(), name='password_change_done'),
    path('user/new', views.UserCreateView.as_view(), name='user_new'),
    path('user/list', views.UserListView.as_view(), name='user_table'),
    path('workers/list', views.WorkersListView.as_view(), name='workers_table'),
]