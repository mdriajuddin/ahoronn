from django.shortcuts import render

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View

from catalog.models import  Medicine
from .models import OrderItem, Order




class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")



class CheckoutView(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        return render(self.request,'order/checkout.html')







@login_required
def add_to_cart(request, pk):
    print(pk)
    medicine = get_object_or_404(Medicine, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        medicine=medicine,
        user=request.user,
        ordered=False

    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(medicine__pk=medicine.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("order:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("order:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("order:order-summary")






@login_required
def remove_from_cart(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(medicine__pk=medicine.pk).exists():
            order_item = OrderItem.objects.filter(
                medicine=medicine,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("order:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("catalog:medicine_details", pk=pk)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("catalog:medicine_details", pk=pk)






@login_required
def remove_single_item_from_cart(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(medicine__pk=medicine.pk).exists():
            order_item = OrderItem.objects.filter(
                medicine=medicine,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("order:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("catalog:medicine_details", pk=pk)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("catalog:medicine_details", pk=pk)