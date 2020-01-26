from django.urls import path

from .views import (
    ItemDetailView,
    checkout,
    HomeView,
    add_to_cart,
    remove_from_cart

)
from django.conf.urls.static import static,settings
from django.contrib.staticfiles.urls import static
from . import views
app_name='OnlineShop'
urlpatterns = [
    path('',HomeView.as_view(),name='item-list'),
    path('checkout/',checkout,name='checkout'),
    path('products/<slug>/',ItemDetailView.as_view(),name='products'),
    path('add-to-cart/<slug>/',add_to_cart ,name='add-to-cart'),
    path('remove-from-cart/<slug>/',remove_from_cart ,name='remove-from-cart')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
