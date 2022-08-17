from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from posts import views as post_views #importamos las vistas de la app post y la renombramos en el proyecto principal
from users import views as users_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.list_posts, name="feed"),
    path('users/login/', users_views.login_view, name="login"), #nombramos la url para que siempre funciones asi se cambie su contenido
    path('users/logout/', users_views.logout_view, name="logout"),
    path('users/signup/', users_views.signup, name="signup"),
    path('users/me/profile/', users_views.update_profile, name='update_profile'),
    path('posts/new', post_views.create_post, name="new"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
