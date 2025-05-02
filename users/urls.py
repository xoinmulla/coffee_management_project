from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  CustomPasswordResetView, home_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Add this line
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    

]