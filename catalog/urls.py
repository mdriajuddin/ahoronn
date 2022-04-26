from django.urls import path


from .views import HomeView,MedicineDetails,filterView
app_name = 'catalog'
urlpatterns = [

    path('', HomeView.as_view(),name="home"),
    path('<uuid:pk>', MedicineDetails.as_view(),name="medicine_details"),
    path('filter',filterView.as_view(),name='filereView')

]
