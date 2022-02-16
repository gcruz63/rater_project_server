from django.db import models


class Game(models.Model):

    # charfield can hold up to 255 characters
    title = models.CharField(max_length=100)
    # textfield can hold more than 255 characters
    description = models.TextField()
    number_of_players = models.IntegerField()
    estimated_play_time = models.IntegerField()
    age_recommended = models.IntegerField()
