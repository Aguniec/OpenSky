from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="page-home"),
    path('about/', views.about, name="page-about")  # /homepage/about
]
