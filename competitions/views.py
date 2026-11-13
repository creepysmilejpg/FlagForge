from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.db.models import Sum, Count
from django.contrib import messages

from .models import Challenge, Submission
from .forms import FlagSubmissionForm


def challenge_list(request):
    challenges = Challenge.objects.filter(is_published=True)

    return render(
        request,
        "challenge_list.html",
        {"challenges": challenges}
    )


@login_required
def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(
        Challenge,
        id=challenge_id,
        is_published=True
    )

    already_solved = Submission.objects.filter(
        player=request.user,
        challenge=challenge,
        is_correct=True
    ).exists()

    form = FlagSubmissionForm()

    if request.method == "POST" and not already_solved:
        form = FlagSubmissionForm(request.POST)

        if form.is_valid():
            submitted_flag = form.cleaned_data["flag"]

            correct = check_password(
                submitted_flag,
                challenge.flag_hash
            )

            Submission.objects.create(
                player=request.user,
                challenge=challenge,
                is_correct=correct
            )

            if correct:
                messages.success(request, "Correct flag!")
                return redirect("challenge_detail", challenge_id=challenge.id)

            messages.error(request, "Incorrect flag.")

    return render(
        request,
        "challenge_detail.html",
        {
            "challenge": challenge,
            "form": form,
            "already_solved": already_solved,
        }
    )


def leaderboard(request):
    players = (
        Submission.objects
        .filter(is_correct=True)
        .values("player__username")
        .annotate(
            score=Sum("challenge__points"),
            solved=Count("challenge")
        )
        .order_by("-score")
    )

    return render(
        request,
        "leaderboard.html",
        {"players": players}
    )