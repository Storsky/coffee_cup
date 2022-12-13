from django.shortcuts import render
from .models import Profile

def index(request):
    template = 'base.html'
    context = {}
    return render(request, template, context)

def show_all_profiles(request):
    template = 'creators.html'
    
    context = {'profiles': Profile.objects.exclude(user=request.user)}
    return render(request, template, context)
