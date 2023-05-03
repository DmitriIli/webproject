from django.contrib import admin
from django.urls import path, include
from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', views.user, name='user'),
    # path('api/login/', views.issue_token, name='issue_token'),
    path('api/login/', views.auth_login, name='login'),
]
