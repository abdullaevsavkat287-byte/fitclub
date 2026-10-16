
from django.shortcuts import render
from .models import Trainer, Workout
from memberships.models import MembershipPlan


def home(request):
    context = {
        "trainers": Trainer.objects.filter(
            is_active=True
        )[:3],
        "workouts": Workout.objects.filter(
            is_active=True
        )[:3],
        "plans": MembershipPlan.objects.filter(
            is_active=True
        )[:3],
        "trainer_count": Trainer.objects.filter(
            is_active=True
        ).count(),
        "workout_count": Workout.objects.filter(
            is_active=True
        ).count(),
    }
    return render(request, "core/home.html", context)


def trainers(request):
    trainers_list = Trainer.objects.filter(
        is_active=True
    )
    return render(
        request,
        "core/trainers.html",
        {"trainers": trainers_list}
    )


def classes(request):
    workouts = Workout.objects.filter(
        is_active=True
    ).select_related("trainer")

    return render(
        request,
        "core/classes.html",
        {"workouts": workouts}
    )
