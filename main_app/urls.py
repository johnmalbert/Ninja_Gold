from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('reset', views.reset),
    path('farmhouse', views.farmhouse),
    path('cave', views.cave),
    path('house', views.house),
    path('casino', views.casino)
]