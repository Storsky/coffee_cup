from django.shortcuts import render, redirect
from .models import Profile, Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def index(request):
    template = 'feed.html'

    if str(request.user) != 'AnonymousUser':
        posts = Post.objects.exclude(owner=request.user)
    else:
        posts = Post.objects.all()
    context = {'posts': posts}
    if request.method == 'POST':
        if 'like' in request.POST:
            post_id = request.POST.get('like')
            current_post = Post.objects.get(id=post_id)
            current_post.likes.add(request.user)
            current_post.save()
            return redirect(to='feed')
        elif 'dislike' in request.POST:
            post_id = request.POST.get('dislike')
            current_post = Post.objects.get(id=post_id)
            current_post.likes.remove(request.user)
            current_post.save()
            return redirect(to='feed')
        elif 'delete' in request.POST:
            post_id = request.POST.get('delete')
            post_to_delete = Post.objects.get(id=post_id)
            post_to_delete.delete()
            return redirect(to='feed')
    return render(request, template, context)


def show_all_creators(request):
    if str(request.user) == 'AnonymousUser':
        return login_redirect(request)
    template = 'creators.html'
    context = {'profiles': Profile.objects.exclude(user=request.user)}
    return render(request, template, context)


@login_required
def show_profile(request, pk):
    template = 'profile.html'
    form = PostForm()
    profile = Profile.objects.get(pk=pk)
    context = {'profile': profile, 'form': form}

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

        elif 'delete' in request.POST:
            post_id = request.POST.get('delete')
            post_to_delete = Post.objects.get(id=post_id)
            post_to_delete.delete()
            return redirect(f'/creator/{request.user.profile.id}')
        

    return render(request, template, context)

def login_redirect(request):
    return redirect(to='/creators/login')