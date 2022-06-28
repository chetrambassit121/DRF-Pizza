from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Order

class HelloOrderView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Orders"}, status=status.HTTP_200_OK)

class OrderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.OrderCreatiobSerializer

    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        pass 

class OrderDetailView(generics.GenericAPIView):

    def get(self, request, order_id):
        pass 

    def put(self, request, order_id):
        pass 

    def delete(self, request, order_id):
        pass
