"""
URL configuration for coffee_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from coffee import views  # Import your views here


class LogoutViewWithGetAllowed(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),  # Add this line for Django Simple Captcha
    path('', include('users.urls')), 
    path('orders/', include('orders.urls')),  # Include the orders app URLs
    path('coffee/', include('coffee.urls')),
    path('logout/', LogoutViewWithGetAllowed.as_view(), name='logout'),
    path('coffee/<int:pk>/edit/', views.edit_coffee, name='coffee_edit'),
    path('coffee/<int:pk>/delete/', views.delete_coffee, name='coffee_delete'),

] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)