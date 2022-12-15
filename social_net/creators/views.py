from django.shortcuts import render
from .models import Profile, Post

def index(request):
    template = 'feed.html'
    posts = Post.objects.exclude(owner=request.user)
    for post in posts:
        video_id = post.yt_link[32:43]
        post.yt_link = "https://www.youtube.com/embed/"+video_id
    context = {'posts': posts}
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