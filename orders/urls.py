from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HelloOrderView.as_view(), name='hello_order'),
    path('', views.OrderCreateListView.as_view(), name='orders'),
]