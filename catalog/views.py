from django.shortcuts import render

# Create your views here.

from .models import Madicine,Category


from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = Category
    context_object_name = 'Category'
    template_name = "home.html"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     # Add in a QuerySet of all the books
    #
    #     context['madicine'] = obj.madicines.all()
    #     return context


class MadicineDetails(DetailView):
    model = Madicine
    context_object_name = "madicine"
    template_name = 'catalog/madicine_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        medicine = self.object
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        # TODO correct the Name
        context['feedbacks'] = medicine.Madicine.all()
        # TODO related_medicine
        return context
