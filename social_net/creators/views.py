from django.shortcuts import render, redirect
from .models import Profile, Post
from .forms import PostForm

def index(request):
    template = 'feed.html'
    posts = Post.objects.exclude(owner=request.user)
    context = {'posts': posts}
    return render(request, template, context)

def show_all_profiles(request):
    template = 'creators.html'
    
    context = {'profiles': Profile.objects.exclude(user=request.user)}
    return render(request, template, context)


def show_profile(request, pk):
    template = 'profile.html'
    form = PostForm()
    profile = Profile.objects.get(pk=pk)
    context = {'profile' : profile, 'form': form}
    
    if request.method == 'POST':
        if 'follow' in request.POST:
            current_user = request.user.profile
            data = request.POST
            action = data.get('follow')
            if action == 'follow':
                current_user.follows.add(profile)
            elif action == 'unfollow':
                current_user.follows.remove(profile)

        elif 'submit' in request.POST:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.owner = request.user
                post.save()
                return redirect(f'/creator/{request.user.profile.id}')
        form = PostForm()

    return render(request, template, context)
