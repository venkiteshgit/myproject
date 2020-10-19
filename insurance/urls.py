from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insurance/', views.get_insured_details, name='get_insured_details'),
    path('enroll/', views.add_insured_details, name='add_insured_details'),
    path('submit_ensured_details/', views.submit_ensured_details, name='submit_ensured_details/'),
]
