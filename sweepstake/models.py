from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    odds = models.CharField(max_length=20, help_text="e.g. 100/1")
    current_score = models.IntegerField(default=0, help_text="Current tournament score (lower is better)")

    def __str__(self):
        return f"{self.name} ({self.odds})"

class Contestant(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    how_paid = models.CharField(max_length=100, blank=True, null=True)
    payment_email = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.CharField(max_length=40, blank=True, null=True)
    entry_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

class Pick(models.Model):
    contestant = models.ForeignKey(Contestant, on_delete=models.CASCADE, related_name="picks")
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def clean(self):
        # Enforce odds >= 100/1
        try:
            odds_val = int(self.player.odds.split('/')[0])
        except Exception:
            odds_val = 0
        if odds_val < 100:
            from django.core.exceptions import ValidationError
            raise ValidationError("Player odds must be at least 100/1.")

    def __str__(self):
        return f"{self.contestant.name} pick: {self.player.name} ({self.player.odds})"
