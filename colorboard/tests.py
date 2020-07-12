from django.test import TestCase
from .game_session import GameSession

game_session_case_with_winner = "Player 2 won after 12 cards."
game_session_case_without_winner = "No player won after 20 cards."


class GameSessionTestCase(TestCase):

    def test_game_session(self):
        test_first_data = {
            "players": 2,
            "squares": 10,
            "deck_size": 20,
            "sequence": "ABACABCCAB",
            "deck_list": "A,B,B,A,A,B,A,C,C,A,B,A,C,A,B,B,A,A,C,A"
        }
        test_session = GameSession(test_first_data)
        test_session.calculate_result()
        self.assertEqual(game_session_case_with_winner, test_session.result)

        test_second_data = {
            "players": 2,
            "squares": 20,
            "deck_size": 20,
            "sequence": "ABACBAACCBABACBAABBB",
            "deck_list": "A,B,B,A,A,B,A,C,C,A,B,A,C,A,B,B,A,B,B,B"
        }
        test_session = GameSession(test_second_data)
        test_session.calculate_result()
        self.assertEqual(game_session_case_without_winner, test_session.result)
