from django.urls import path


from .views import HomeView,MedicineDetails
app_name = 'catalog'
urlpatterns = [

    path('', HomeView.as_view(),name="home"),
    path('<uuid:pk>', MedicineDetails.as_view(),name="medicine_details"),

]
