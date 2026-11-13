from django.contrib import admin
from .models import Challenge, Submission
from .forms import ChallengeAdminForm


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    form = ChallengeAdminForm

    list_display = (
        "title",
        "category",
        "points",
        "is_published",
    )

    list_filter = ("category", "is_published")
    search_fields = ("title",)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "player",
        "challenge",
        "is_correct",
        "submitted_at",
    )

    list_filter = ("is_correct",)