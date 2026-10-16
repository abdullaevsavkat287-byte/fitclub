
from django.contrib import admin, messages
from django.db import transaction
from django.utils import timezone
from datetime import timedelta

from .models import MembershipPlan, Subscription


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "duration_days",
        "is_popular",
        "is_active",
    )
    list_editable = ("is_popular", "is_active")
    search_fields = ("name",)


@admin.action(description="Tanlangan obunalarni faollashtirish")
def activate_subscriptions(modeladmin, request, queryset):
    activated = 0
    skipped = 0

    for subscription_id in queryset.values_list(
        "id", flat=True
    ):
        with transaction.atomic():
            sub = Subscription.objects.select_for_update().get(
                pk=subscription_id
            )

            if sub.status != "pending":
                skipped += 1
                continue

            today = timezone.localdate()

            other_active = Subscription.objects.filter(
                user=sub.user,
                status="active",
                start_date__lte=today,
                end_date__gte=today
            ).exclude(pk=sub.pk).exists()

            if other_active:
                skipped += 1
                continue

            sub.activate()
            activated += 1

    modeladmin.message_user(
        request,
        f"{activated} ta obuna faollashtirildi. "
        f"{skipped} ta obuna o'tkazib yuborildi.",
        messages.SUCCESS
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "plan",
        "status",
        "start_date",
        "end_date",
        "remaining_days",
        "created_at",
    )
    list_filter = ("status", "plan")
    search_fields = (
        "user__username",
        "user__email",
    )
    readonly_fields = ("created_at",)
    actions = [activate_subscriptions]

    @admin.display(description="Qolgan kun")
    def remaining_days(self, obj):
        return obj.days_left
