from django.urls import path

from .views import SearchResultView


urlpatterns = [
    path('',SearchResultView.as_view(),name='search_result')


]