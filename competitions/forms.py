from django import forms
from django.contrib.auth.hashers import make_password
from .models import Challenge


class FlagSubmissionForm(forms.Form):
    flag = forms.CharField(
        max_length=255,
        label="Enter Flag",
        widget=forms.TextInput(attrs={
            "placeholder": "flag{...}"
        })
    )


class ChallengeAdminForm(forms.ModelForm):
    flag = forms.CharField(
        label="Challenge Flag",
        widget=forms.PasswordInput,
        help_text="Enter the correct flag for this challenge."
    )

    class Meta:
        model = Challenge
        fields = [
            "title",
            "description",
            "category",
            "points",
            "is_published",
        ]

    def save(self, commit=True):
        challenge = super().save(commit=False)
        challenge.flag_hash = make_password(
            self.cleaned_data["flag"]
        )

        if commit:
            challenge.save()

        return challenge