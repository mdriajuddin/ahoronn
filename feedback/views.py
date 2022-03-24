from django.shortcuts import render


from .models import Feedback
from catalog.models import Madicine
# Create your views here.
from django.views.generic import CreateView, UpdateView,DeleteView
from django.views import View
from django.shortcuts import redirect

class FeedbackCreateView(View):
    def post(self,request,*args, **kwargs):
        content = self.request.POST.get('content')
        if content is not None:
            madicine = self.request.POST.get('madicine')
            m = Madicine.objects.get(pk=madicine)
            Feedback.objects.create(feedback_content=content,creator=request.user,madicine=m)
            return redirect('catalog:madicine_details', m.pk)

