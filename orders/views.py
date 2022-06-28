from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

class HelloOrderView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Orders"}, status=status.HTTP_200_OK)

class OrderCreateListView(generics.GenericAPIView):

    def get(self, request):
        pass 

    def post(self, request):
        pass 

class OrderDetailView(generics.GenericAPIView):

    def get(self, request, order_id):
        pass 

    def put(self, request, order_id):
        pass 

    def delete(self, request, order_id):
        pass
