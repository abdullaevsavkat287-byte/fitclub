
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        label="Ism"
    )
    last_name = forms.CharField(
        max_length=100,
        label="Familiya"
    )
    email = forms.EmailField(
        required=True,
        label="Email"
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Bu email allaqachon ro‘yxatdan o‘tgan."
            )

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
            Profile.objects.get_or_create(user=user)

        return user
