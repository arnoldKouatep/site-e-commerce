from django.urls import path
from shop.views import checkout, confirmation, detail, index

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail, name='detail'),
    path('checkout', checkout, name='checkout'),
    path('confirmation', confirmation, name='confirmation'),
]
