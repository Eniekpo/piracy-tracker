from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Frontend
    path('', views.frontend, name="frontend"),
    # Backend
    path('backend/', views.backend, name="backend"),
    # Login/Logout
    path('login/', include('django.contrib.auth.urls')),

   path('result/', views.result, name="result"),
]
