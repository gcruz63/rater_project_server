from django.db import models


class Category(models.Model):
    # label is a variable with a 1 to 1 key in the database
    label = models.CharField(max_length=50)
