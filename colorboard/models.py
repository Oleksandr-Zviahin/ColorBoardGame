from django.db import models


class GameHistory(models.Model):
    players = models.IntegerField()
    squares = models.IntegerField()
    deck_size = models.IntegerField()
    deck_list = models.CharField(max_length=1000)
    sequence = models.CharField(max_length=200)
    result = models.CharField(max_length=100)
    session_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.result}, " \
               f"session_info: [{self.players}, {self.squares}, {self.deck_size}]]>," \
               f"session_date: {self.session_date}"
