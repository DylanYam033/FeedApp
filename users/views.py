"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout #importamos libreria o modulos para autenticar usuario y logear
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User #modelo para crear usuario
from users.models import Profile

# Forms
from users.forms import ProfileForm


@login_required #decorador para asegurar que haya una sesion iniciada
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )



def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'}) #nos deja en la misma url pero con el mensaje de error

    return render(request, 'users/login.html') 


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')


def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username'] #en los corchetes va el name que se definiio en el html de signup
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation: #validamos que las contraseñas sean iguales
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)#creamos el usurio e importamos el modelo para hacerlo
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user) #instancia del modelo profile y le pasamos user que se acabo de crear para que cree un profile con los datos que se ingresaron desde el html de signup
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')