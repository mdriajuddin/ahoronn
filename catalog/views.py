from django.shortcuts import render

# Create your views here.

from .models import Medicine,Category
from django.db.models import Q

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


class MedicineDetails(DetailView):
    model = Medicine
    context_object_name = "medicine"
    template_name = 'catalog/medicine_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        medicine = self.object
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        # TODO correct the Name
        context['feedbacks'] = medicine.feedback.all()
        # TODO related_medicine
        return context

class filterView(ListView):
    model = Category
    context_object_name = 'madicine_list'
    template_name = 'filter_result.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            c = Category.objects.get(category_title=query)
            return c.medicines.all()
