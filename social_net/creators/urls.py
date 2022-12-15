from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('creators', show_all_profiles),
    path('creator/<int:pk>', show_profile, name='profile')


]