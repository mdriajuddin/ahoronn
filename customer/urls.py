from django.urls import path

from .views import Profile_View


app_name = 'customer'
urlpatterns = [
    path('',Profile_View,name='profile')
]