from django.shortcuts import render

from catalog.models import Madicine
from .models import Search

from django.db.models import Q
from django.views.generic import ListView
# Create your views here.


class SearchResultView(ListView):
    model = Madicine
    context_object_name = 'madicine_list'
    template_name = 'search/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            Search.objects.create(keyword=query)
            return Madicine.objects.filter(Q(trade_name__icontains=query))
