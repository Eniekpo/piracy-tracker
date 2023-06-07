from django.urls import path
from . import views

urlpatterns = [
    path('breg', views.breg, name='breg'),
    path('vreg', views.vreg, name='vreg'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
