from django.db import models


class Review(models.Model):
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
    review = models.IntegerField()
