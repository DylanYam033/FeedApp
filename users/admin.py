from django.contrib import admin
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ("pk", "user", "phone_number", "website")
    search_fields = ("user__email", "user__first_name", "user__last_name")

    list_filter = ("modified", "created")
