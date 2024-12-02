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
    
    def carrotsOther(self) -> int:
        return self.game_state.clone_other_player().carrots

    # this method is called every time the server is requesting a new move
    # this method should always be implemented otherwise the client will be disqualified
    def calculate_move(self) -> Move:

        # Variable für alle possible Moves
        poss = self.game_state.possible_moves()

        # Gib alle Felder
        fields = self.game_state.board.track

        # Stats eigener Spieler
        player = self.game_state.clone_current_player()

        # Karotten anderer Spieler in neuer Methode
        carrots = self.carrotsOther()
        
        # Ob ein spezieller Feldtyp in Reichweite ist
        for p in poss:
            if "advance" in type(p.action):
                if self.game_state.board.get_field(player.position + p.action.distance) == Field.Salad:
                    print(p)
        
        # Noch eine Idee?

        return random.choice(poss)

    # this method is called every time the server has sent a new game state update
    # this method should be implemented to keep the game state up to date
    def on_update(self, state: GameState) -> None:
        self.game_state = state


if __name__ == "__main__":
    Starter(logic=Logic())
    # if u wanna have more insights, u can set the logging level to debug:
    # Starter(logic=Logic(), log_level=logging.DEBUG)