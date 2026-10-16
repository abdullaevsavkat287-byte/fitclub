
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db import transaction
from django.utils import timezone

from .models import MembershipPlan, Subscription


def plans(request):
    all_plans = MembershipPlan.objects.filter(
        is_active=True
    )

    return render(
        request,
        "memberships/plans.html",
        {"plans": all_plans}
    )


@login_required
@require_POST
def subscribe(request, plan_id):
    plan = get_object_or_404(
        MembershipPlan,
        id=plan_id,
        is_active=True
    )

    with transaction.atomic():
        # Bir foydalanuvchining parallel so'rovlarini
        # ketma-ket qayta ishlash uchun user qatorini qulflaymiz.
        from django.contrib.auth.models import User
        User.objects.select_for_update().get(
            pk=request.user.pk
        )

        today = timezone.localdate()

        has_active = Subscription.objects.filter(
            user=request.user,
            status="active",
            start_date__lte=today,
            end_date__gte=today
        ).exists()

        has_pending = Subscription.objects.filter(
            user=request.user,
            status="pending"
        ).exists()

        if has_active:
            messages.warning(
                request,
                "Sizda allaqachon faol obuna mavjud."
            )
            return redirect("dashboard")

        if has_pending:
            messages.warning(
                request,
                "Oldingi obuna so‘rovingiz hali ko‘rib chiqilmoqda."
            )
            return redirect("dashboard")

        Subscription.objects.create(
            user=request.user,
            plan=plan,
            status="pending"
        )

    messages.success(
        request,
        "Obuna so‘rovingiz yuborildi! Admin tasdiqlashini kuting."
    )

    return redirect("dashboard")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db import transaction
from django.utils import timezone

from .models import MembershipPlan, Subscription


def plans(request):
    all_plans = MembershipPlan.objects.filter(
        is_active=True
    )

    return render(
        request,
        "memberships/plans.html",
        {"plans": all_plans}
    )


@login_required
@require_POST
def subscribe(request, plan_id):
    plan = get_object_or_404(
        MembershipPlan,
        id=plan_id,
        is_active=True
    )

    with transaction.atomic():
        # Bir foydalanuvchining parallel so'rovlarini
        # ketma-ket qayta ishlash uchun user qatorini qulflaymiz.
        from django.contrib.auth.models import User
        User.objects.select_for_update().get(
            pk=request.user.pk
        )

        today = timezone.localdate()

        has_active = Subscription.objects.filter(
            user=request.user,
            status="active",
            start_date__lte=today,
            end_date__gte=today
        ).exists()

        has_pending = Subscription.objects.filter(
            user=request.user,
            status="pending"
        ).exists()

        if has_active:
            messages.warning(
                request,
                "Sizda allaqachon faol obuna mavjud."
            )
            return redirect("dashboard")

        if has_pending:
            messages.warning(
                request,
                "Oldingi obuna so‘rovingiz hali ko‘rib chiqilmoqda."
            )
            return redirect("dashboard")

        Subscription.objects.create(
            user=request.user,
            plan=plan,
            status="pending"
        )

    messages.success(
        request,
        "Obuna so‘rovingiz yuborildi! Admin tasdiqlashini kuting."
    )

    return redirect("dashboard")
