
from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=12,
        decimal_places=0
    )
    duration_days = models.PositiveIntegerField(default=30)
    features = models.TextField(
        help_text="Har bir imkoniyatni yangi qatordan yozing"
    )
    is_popular = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["price"]
        verbose_name = "Abonement tarifi"
        verbose_name_plural = "Abonement tariflari"

    def __str__(self):
        return self.name

    @property
    def feature_list(self):
        return [
            item.strip()
            for item in self.features.splitlines()
            if item.strip()
        ]


class Subscription(models.Model):
    STATUS_CHOICES = [
        ("pending", "Kutilmoqda"),
        ("active", "Faol"),
        ("expired", "Tugagan"),
        ("cancelled", "Bekor qilingan"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscriptions"
    )
    plan = models.ForeignKey(
        MembershipPlan,
        on_delete=models.PROTECT
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    start_date = models.DateField(
        null=True,
        blank=True
    )
    end_date = models.DateField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Obuna"
        verbose_name_plural = "Obunalar"

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"

    @property
    def days_left(self):
        if self.status != "active" or not self.end_date:
            return 0

        difference = (
            self.end_date - timezone.localdate()
        ).days

        return max(0, difference)

    @property
    def is_valid(self):
        return (
            self.status == "active"
            and self.start_date is not None
            and self.end_date is not None
            and self.start_date <= timezone.localdate()
            and self.end_date >= timezone.localdate()
        )

    @property
    def progress(self):
        if not self.start_date or not self.end_date:
            return 0

        total = (self.end_date - self.start_date).days
        if total <= 0:
            return 0

        remaining = max(
            0,
            (self.end_date - timezone.localdate()).days
        )

        return round(
            max(0, min(100, remaining * 100 / total))
        )

    @property
    def display_status(self):
        if self.status == "active" and not self.is_valid:
            return "expired"
        return self.status

    def activate(self):
        today = timezone.localdate()
        self.start_date = today
        self.end_date = (
            today + timedelta(days=self.plan.duration_days)
        )
        self.status = "active"
        self.save()
