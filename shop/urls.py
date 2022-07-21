from django.urls import path
from shop.views import checkout, confirmation, detail, index, listes_produit

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail, name='detail'),
    path('checkout', checkout, name='checkout'),
    path('confirmation', confirmation, name='confirmation'),
    path('listes_produit', listes_produit, name='listes_produit'),
]
