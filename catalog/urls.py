from django.urls import path


from .views import HomeView,MadicineDetails
app_name = 'catalog'
urlpatterns = [

    path('', HomeView.as_view(),name="home"),
    path('<uuid:pk>', MadicineDetails.as_view(),name="madicine_details"),

]
