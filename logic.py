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

        hedges = [11, 15, 19, 24, 30, 37, 43, 50, 56]
        salads = [10, 20, 42, 57]

        counter = 0
        hedge_counter = 0
        salad_counter = 0
        error = False
        for f in self.game_state.board.track:

            if f == Field.Hedgehog:
                hedge_counter += 1
                if counter not in hedges:
                    print("got wrong hedgehog at position:", counter)
                    error = True
                
            if f == Field.Salad:
                salad_counter += 1
                if counter not in salads:
                    print("got wrong salad at position:", counter)
                    error = True

            counter += 1

        if hedge_counter != len(hedges):
            print("got wrong amount of hedgehogs:", hedge_counter)
        elif salad_counter != len(salads):
            print("got wrong amount of salats:", salad_counter)
        else:
            if not error:
                print("every field where it should be")

        return random.choice(self.game_state.possible_moves())

    # this method is called every time the server has sent a new game state update
    # this method should be implemented to keep the game state up to date
    def on_update(self, state: GameState) -> None:
        self.game_state = state


if __name__ == "__main__":
    Starter(logic=Logic())
    # if u wanna have more insights, u can set the logging level to debug:
    # Starter(logic=Logic(), log_level=logging.DEBUG)