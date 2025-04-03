from django.urls import path
from . import views

urlpatterns = [
    path('', views.allChai, name='allChai'),
    path('order/', views.order, name='order'),
    # path('contact/', views.contact, name='contact'),
]
