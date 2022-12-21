from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="feed"),
    path('creators', show_all_creators, name="creators"),
    path('creator/', login_redirect),
    path('creator/<int:pk>', show_profile, name='profile'),
    path('creators/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('creators/signup', register),


]