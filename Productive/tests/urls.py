from django.urls import path
from . import views  # Import the view

urlpatterns = [
    path('', views.main, name="main"),
    path('workers/', views.test_view, name='test_views'),
    path('more/', views.more, name="more"),
    path('workers/details/<int:id>', views.details, name='details'), 
    path('testing/', views.testing, name="testing"),
]
