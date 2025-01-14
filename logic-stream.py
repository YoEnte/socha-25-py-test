# not all imports are currently used, but they might be in the future and it shows all available functionalities
import math
import random
import time
from typing import Optional, Tuple
from socha import (
    Field,
    GameState,
    Move,
    Advance,
    EatSalad,
    ExchangeCarrots,
    FallBack,
    Card,
    Board,
    Hare,
    TeamEnum
)
from socha.api.networking.game_client import IClientHandler
from socha.starter import Starter


class Logic(IClientHandler):
    game_state: GameState

    # list of all fields with _type FieldType (e.g. Field.Salad)
    def getFieldTypeIndeces(self, _type):

        liste = []

        i = 0
        for f in self.game_state.board.track:
            if f == _type:
                liste.append(i)
            i += 1

        return liste
    
    # list all distances of possible moves
    def getTurnDistances(self):

        poss = self.game_state.possible_moves()

        liste = []

        for move in poss:
            if isinstance(move.action, Advance):
                liste.append(move.action.distance)

        return liste
    
    # get fallback distance
    def getFallbackDistance(self):

        distance = 0

        playerPos = self.game_state.clone_current_player().position

        for i in range(playerPos, 0, -1):
            if self.game_state.board.get_field(i) == Field.Hedgehog:
                return playerPos - i
    
    # count cards of player
    def countCards(self, cardType: Card) -> int:

        i = 0

        for card in self.game_state.clone_current_player().cards:
            if card == cardType:
                i += 1

        return i
    
    def countAllCards(self):

        cards = {
            "FallBack": self.countCards(Card.FallBack),
            "HurryAhead": self.countCards(Card.HurryAhead),
            "EatSalad": self.countCards(Card.EatSalad),
            "SwapCarrots": self.countCards(Card.SwapCarrots),
        }

        return cards
    
    # get technically max turn distance based of cards
    def maxTurnLength(self):

        _sum = 0

        for i in range(1, 50):

            _sum += i

            if _sum > self.game_state.clone_current_player().carrots:
                break

        return i - 1


    # this method is called every time the server is requesting a new move
    # this method should always be implemented otherwise the client will be disqualified
    def calculate_move(self) -> Move:

        print(self.maxTurnLength())

        return random.choice(self.game_state.possible_moves())

    # this method is called every time the server has sent a new game state update
    # this method should be implemented to keep the game state up to date
    def on_update(self, state: GameState) -> None:
        self.game_state = state


if __name__ == "__main__":
    Starter(logic=Logic())
    # if u wanna have more insights, u can set the logging level to debug:
    # Starter(logic=Logic(), log_level=logging.DEBUG)