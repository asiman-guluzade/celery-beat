from django.urls import path

from djangocelery import views

urlpatterns = [
    path('mod', views.get_test_add),
]