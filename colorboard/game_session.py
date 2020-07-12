from .models import GameHistory


class GameSession:
    def __init__(self, settings):
        self.players = settings['players']
        self.squares = settings['squares']
        self.deck_size = settings['deck_size']
        self.sequence = settings['sequence'].upper()
        self.deck_list = settings['deck_list'].upper().replace(' ', '').split(',')
        self.result = f'No player won after {self.deck_size} cards.'
        self.is_game_end = False
        if len(self.deck_list) != self.deck_size:
            raise Exception(f'Deck size not equal to deck list size: {self.deck_size} != {self.deck_list}')

    def save_session(self):
        GameHistory(players=self.players, squares=self.squares, deck_size=self.deck_size,
                    deck_list=self.deck_list, sequence=self.sequence, result=self.result).save()

    @staticmethod
    def current_player_info(player, deck):
        """
        :param player: range of players
        :param deck: deck with cards
        :return: generator object with players and deck info
        """
        player_index = 0
        card_index = 0

        while card_index < len(deck):
            yield card_index, player[player_index], deck[card_index]
            player_index = 0 if player_index + 1 >= len(player) else player_index + 1
            card_index += 1

    def calculate_result(self):
        players = range(1, self.players + 1)
        players_pos = dict((x, -1) for x in players)

        for index, player, cards in self.current_player_info(players, self.deck_list):
            for card in cards:
                found = self.sequence.find(card, players_pos[player] + 1)
                if found < 0 or found+1 == self.squares:  # we need to add 1 to our found because we work with 0 index
                    self.result = f'Player {player} won after {index+1} cards.'
                    self.is_game_end = True
                    break
                players_pos[player] = found

            if self.is_game_end:
                break

        self.save_session()
