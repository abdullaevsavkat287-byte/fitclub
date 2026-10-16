
from django.db import models


class Trainer(models.Model):
    SPECIALTIES = [
        ("yoga", "Yoga"),
        ("cardio", "Kardio"),
        ("strength", "Og‘ir atletika"),
        ("fitness", "Fitness"),
        ("personal", "Personal trener"),
    ]

    full_name = models.CharField(max_length=150)
    specialty = models.CharField(
        max_length=30,
        choices=SPECIALTIES
    )
    experience = models.PositiveIntegerField(default=1)
    description = models.TextField()
    image = models.ImageField(
        upload_to="trainers/",
        blank=True,
        null=True
    )
    instagram = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["full_name"]
        verbose_name = "Trener"
        verbose_name_plural = "Trenerlar"

    def __str__(self):
        return self.full_name


class Workout(models.Model):
    LEVELS = [
        ("beginner", "Boshlang‘ich"),
        ("intermediate", "O‘rta"),
        ("advanced", "Professional"),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField()
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workouts"
    )
    duration = models.PositiveIntegerField(
        default=60,
        help_text="Daqiqalarda"
    )
    level = models.CharField(
        max_length=20,
        choices=LEVELS,
        default="beginner"
    )
    image = models.ImageField(
        upload_to="workouts/",
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Mashg‘ulot"
        verbose_name_plural = "Mashg‘ulotlar"

    def __str__(self):
        return self.title
