from django.urls import path

from .views import FeedbackCreateView #FeedbackEditView,FeedbackDeleteView

app_name = 'feedback'

urlpatterns = [
    path('create/',FeedbackCreateView.as_view(),name="FeedbackCreate"),
]