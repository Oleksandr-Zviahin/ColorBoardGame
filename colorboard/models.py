from django.db import models


class GameHistory(models.Model):
    players = models.IntegerField()
    squares = models.IntegerField()
    deck_size = models.IntegerField()
    deck_list = models.CharField(max_length=1000)
    sequence = models.CharField(max_length=200)
    result = models.CharField(max_length=100)
