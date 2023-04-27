from django.contrib import admin
from django.urls import path
from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', views.user, name='user'),
    path('api/login', views.issue_token, name='issue_token'),
]
