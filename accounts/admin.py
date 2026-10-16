
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "joined_at")
    search_fields = (
        "user__username",
        "user__email",
        "phone",
    )
    readonly_fields = ("joined_at",)
