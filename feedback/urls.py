from django.urls import path

from .views import FeedbackCreateView #FeedbackEditView,FeedbackDeleteView

urlpatterns = [
    path('create/',FeedbackCreateView.as_view(),name="FeedbackCreate"),
    # path('<uuid:pk>/edit',FeedbackEditView.as_view(),name='FeedbackEdit'),
    # path('<uuid:pk>/delete',FeedbackDeleteView,name='FeedbackDelte'),
]