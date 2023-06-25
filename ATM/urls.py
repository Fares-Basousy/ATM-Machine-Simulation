from django.urls import path

from . import views

urlpatterns = [
    path('details/',views.details, name='details'),
    path('details/operations', views.operations),
    path('deposit/', views.deposit),
    path('withdrawal/', views.withdrawal),

]