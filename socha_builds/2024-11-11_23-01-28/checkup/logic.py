# not all imports are currently used, but they might be in the future and it shows all available functionalities
import math
import random
import time
from typing import Optional, Tuple
from socha import (
    Field,
    GameState,
    Move
)
from socha.api.networking.game_client import IClientHandler
from socha.starter import Starter


class Logic(IClientHandler):
    game_state: GameState

    # this method is called every time the server is requesting a new move
    # this method should always be implemented otherwise the client will be disqualified
    def calculate_move(self) -> Move:

        poss = self.game_state.possible_moves();
        

        return random.choice(poss)

    # this method is called every time the server has sent a new game state update
    # this method should be implemented to keep the game state up to date
    def on_update(self, state: GameState) -> None:
        self.game_state = state

        poss = self.game_state.possible_moves();

        print("\n\n")
        print("turn:", self.game_state.turn)
        print(self.game_state.clone_current_player())
        print(self.game_state.clone_other_player())
        for p in poss:
            print(p)

if __name__ == "__main__":
    Starter(logic=Logic())
    # if u wanna have more insights, u can set the logging level to debug:
    # Starter(logic=Logic(), log_level=logging.DEBUG)