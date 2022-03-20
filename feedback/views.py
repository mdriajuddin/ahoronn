from django.shortcuts import render


from .models import Feedback
# Create your views here.
from django.views.generic import CreateView, UpdateView,DeleteView

class FeedbackCreateView(CreateView):
    model = Feedback

    template_name = 'feedback/feedback_create.html'

# class FeedbackEditView(UpdateView):
#     pass
#
# class FeedbackDeleteView(DeleteView):
#     pass



