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


def show_profile(request, pk):
    template = 'profile.html'
    profile = Profile.objects.get(pk=pk)
    context = {'profile' : profile}
    if request.method == 'POST':
        current_user = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user.follows.add(profile)
        elif action == 'unfollow':
            current_user.follows.remove(profile)

    return render(request, template, context)