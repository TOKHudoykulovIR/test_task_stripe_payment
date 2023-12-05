from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from django.conf import settings
from .serializers import OrderSerializer
from orders.models import Order
from decimal import Decimal
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


class OrderCheckoutView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, *args, **kwargs):
        order = self.get_object()

        session_data = {
            'mode': 'payment',
            'success_url': request.build_absolute_uri(order.get_absolute_url()),
            'cancel_url': request.build_absolute_uri(order.get_absolute_url()),
            'line_items': [],
        }

        for order_item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    'unit_amount': int(order_item.price * Decimal('100')),
                    'currency': 'usd',
                    'product_data': {
                        'name': order_item.item.name,
                    },
                },
                'quantity': order_item.quantity,
            })
        session = stripe.checkout.Session.create(**session_data)

        return Response({'session_id': session.id})


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        return render(request, 'shop/order_detail.html', {'order': instance})
