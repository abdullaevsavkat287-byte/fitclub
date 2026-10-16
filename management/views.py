
from django.apps import apps
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.shortcuts import render

from core.models import Trainer, Workout
from memberships.models import MembershipPlan, Subscription


@staff_member_required(login_url="login")
def dashboard(request):
    User = get_user_model()

    context = {
        "total_users": User.objects.count(),
        "total_trainers": Trainer.objects.count(),
        "total_workouts": Workout.objects.count(),
        "total_plans": MembershipPlan.objects.count(),
        "active_subscriptions": 0,
        "pending_subscriptions": 0,
        "expiring_subscriptions": 0,
        "recent_subscriptions": Subscription.objects.none(),
        "recent_users": User.objects.order_by("-date_joined")[:6],
    }

    return render(
        request,
        "management/dashboard.html",
        context
    )


MANAGED_MODELS = {
    "users": {
        "model": apps.get_model("auth", "User"),
        "title": "Foydalanuvchilar",
        "search": ["username", "email", "first_name", "last_name"],
        "editable": False,
    },
    "subscriptions": {
        "model": apps.get_model("memberships", "Subscription"),
        "title": "Obunalar",
        "search": [],
        "editable": False,
    },
    "plans": {
        "model": apps.get_model("memberships", "MembershipPlan"),
        "title": "Tariflar",
        "search": ["name"],
        "editable": True,
    },
    "trainers": {
        "model": apps.get_model("core", "Trainer"),
        "title": "Trenerlar",
        "search": [],
        "editable": True,
    },
    "workouts": {
        "model": apps.get_model("core", "Workout"),
        "title": "Treninglar",
        "search": [],
        "editable": True,
    },
}


def get_section(section):
    config = MANAGED_MODELS.get(section)

    if not config:
        raise Http404("Bunday bo‘lim mavjud emas.")

    return config


@staff_member_required(login_url="login")
def records_list(request, section):
    config = get_section(section)
    model = config["model"]

    queryset = model.objects.all().order_by("-pk")
    search = request.GET.get("q", "").strip()[:100]

    if search and config["search"]:
        query = Q()

        for field in config["search"]:
            query |= Q(**{f"{field}__icontains": search})

        queryset = queryset.filter(query)

    paginator = Paginator(queryset, 12)
    page = paginator.get_page(request.GET.get("page"))

    return render(request, "management/records.html", {
        "section": section,
        "section_title": config["title"],
        "page": page,
        "search": search,
        "editable": config["editable"] and request.user.is_superuser,
        "has_search": bool(config["search"]),
    })


@staff_member_required(login_url="login")
def record_form(request, section, pk=None):
    config = get_section(section)

    if not request.user.is_superuser or not config["editable"]:
        raise Http404("Tahrirlashga ruxsat yo‘q.")

    model = config["model"]
    instance = get_object_or_404(model, pk=pk) if pk else None

    FormClass = modelform_factory(model, fields="__all__")

    if request.method == "POST":
        form = FormClass(
            request.POST,
            request.FILES,
            instance=instance
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Ma'lumot saqlandi.")
            return redirect("management:records", section=section)
    else:
        form = FormClass(instance=instance)

    return render(request, "management/record_form.html", {
        "form": form,
        "section": section,
        "section_title": config["title"],
        "editing": instance is not None,
    })


@staff_member_required(login_url="login")
@require_POST
def record_delete(request, section, pk):
    config = get_section(section)

    if not request.user.is_superuser or not config["editable"]:
        raise Http404("O‘chirishga ruxsat yo‘q.")

    obj = get_object_or_404(config["model"], pk=pk)
    obj.delete()

    messages.success(request, "Ma'lumot o‘chirildi.")
    return redirect("management:records", section=section)
