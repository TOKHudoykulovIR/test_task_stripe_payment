from django.urls import path
from .views import OrderCheckoutView, OrderDetailView

app_name = 'api'

urlpatterns = [
    path('buy/<int:pk>/', OrderCheckoutView.as_view(), name='buy-item'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='item-detail'),
]

