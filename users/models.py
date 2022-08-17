from django.db import models
from django.contrib.auth.models import User #heredamos de una clase user propia de django

# Create your models here.
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=10)
    biography = models.TextField(max_length=200, blank=True)
    picture = models.ImageField(upload_to="users/pictures", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username 