from django.urls import path

from .views import PescriptionCreateView

app_name = "pescription"

urlpatterns = [
    path('create/',PescriptionCreateView,name='PescriptionCreate'),
]