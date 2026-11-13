from django.urls import path
from . import views

urlpatterns = [
    path("", views.challenge_list, name="challenge_list"),
    path(
        "challenge/<int:challenge_id>/",
        views.challenge_detail,
        name="challenge_detail",
    ),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
]