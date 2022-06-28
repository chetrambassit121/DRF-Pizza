from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Order
from rest_framework.permissions import IsAuthenticated 

class HelloOrderView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Orders"}, status=status.HTTP_200_OK)

class OrderCreateListView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()
    permission_classes=[IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data=request.data
        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(customer=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   

class OrderDetailView(generics.GenericAPIView):

    def get(self, request, order_id):
        order=get_object_or_404(Order, pk=order_id)

        
        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        pass 

    def delete(self, request, order_id):
        pass
