from django.db import models
from django.contrib.auth.models import User


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    points = models.IntegerField(default=100)
    flag_hash = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Submission(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["player", "challenge"],
                condition=models.Q(is_correct=True),
                name="unique_correct_submission",
            )
        ]

    def __str__(self):
        return f"{self.player.username} - {self.challenge.title}"