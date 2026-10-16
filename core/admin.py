
from django.contrib import admin
from .models import Trainer, Workout


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "specialty",
        "experience",
        "is_active",
    )
    list_filter = ("specialty", "is_active")
    search_fields = ("full_name", "description")
    list_editable = ("is_active",)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "trainer",
        "duration",
        "level",
        "is_active",
    )
    list_filter = ("level", "is_active")
    search_fields = ("title",)
    list_editable = ("is_active",)
