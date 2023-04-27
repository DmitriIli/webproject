from django.contrib import admin
from django.urls import path
from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', views.user, name='user'),
    path('api/login', views.login, name='login'),
]
