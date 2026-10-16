
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .forms import RegisterForm
from .models import Profile
from memberships.models import Subscription


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                "FitClub'ga xush kelibsiz!"
            )
            return redirect("dashboard")
    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


@login_required
def dashboard(request):
    profile, _ = Profile.objects.get_or_create(
        user=request.user
    )

    subscriptions = Subscription.objects.filter(
        user=request.user
    ).select_related("plan")

    today = timezone.localdate()

    active_subscription = subscriptions.filter(
        status="active",
        start_date__lte=today,
        end_date__gte=today
    ).order_by("-end_date").first()

    pending_subscription = subscriptions.filter(
        status="pending"
    ).first()

    context = {
        "profile": profile,
        "subscriptions": subscriptions,
        "active_subscription": active_subscription,
        "pending_subscription": pending_subscription,
        "subscription_count": subscriptions.count(),
    }

    return render(
        request,
        "accounts/dashboard.html",
        context
    )
