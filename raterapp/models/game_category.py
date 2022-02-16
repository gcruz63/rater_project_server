from django.db import models


class Game_Category(models.Model):
    # When you have a foreignKey and do on_delete CASCADE it deletes the foreign from the model it came from
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
