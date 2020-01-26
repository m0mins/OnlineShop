from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect,reverse
from .models import Item,OrderItem,Order
from django.utils import timezone
from django.views.generic import ListView,DetailView,View
from django.conf import settings
# Create your views here.


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product-page.html", context)


def checkout(request):
    return render(request,"checkout-page.html")


class HomeView(ListView):
    model=Item
    template_name = "home-page.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"

def add_to_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)
    order_item,created=OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        #Check if the order item is the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "This item quantity was updated  .")
            return redirect("OnlineShop:products", slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart .")
            return redirect("OnlineShop:products", slug=slug)

    else:
        ordered_date = timezone.now()
        order=Order.objects.create(
            user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart .")
        return redirect("OnlineShop:products" ,slug=slug )

def remove_from_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)

    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # Check if the order item is the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item=OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item  was removed from the cart  .")
            return redirect("OnlineShop:products", slug=slug)

        else:
            # add a message saying the user does not have an order
            messages.info(request, "This item  was not in your cart   .")
            return redirect("OnlineShop:products", slug=slug)

    else:
        #add a message saying the user does not have an order
        messages.info(request, " You do not have an active order  .")
        return redirect("OnlineShop:products", slug=slug)








