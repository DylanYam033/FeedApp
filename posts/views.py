"""Posts views."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #sirve para no dejar entrar al feed si no hay una sesion

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm

# Utilities
from datetime import datetime

posts = [ #lista compuesta de diccionarios
    {
        'title': 'Add Description',
        'user': {
            'name': 'Hinami Sakuta',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.ibb.co/t4t8y2G/6.jpg',
    },
    {
        'title': 'Add Description',
        'user': {
            'name': 'Touka Misato',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.ibb.co/6chC49L/7.jpg',
    },
    {
        'title': 'Add Description',
        'user': {
            'name': 'Kana Honiwara',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.ibb.co/k2nC25X/3.jpg',
    }
]

@login_required
def list_posts(request):
    """List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})
    

@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )