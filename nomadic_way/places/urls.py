from django.urls import path
from . import views

urlpatterns = [
    path('sites/', views.sites, name="sites"),
    path('site/<str:pk>/', views.site, name="site"),
]