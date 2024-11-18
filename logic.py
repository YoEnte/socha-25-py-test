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

    def schlauerMove(self):
        return 1
    
    # this method is called every time the server is requesting a new move
    # this method should always be implemented otherwise the client will be disqualified
    def calculate_move(self) -> Move:

        # alles aktuell spielbaren Züge vom eigenen Bot
        poss = self.game_state.possible_moves();

        print("\n\n")

        # aktueller Zug (Zahl)
        print("Zug:", self.game_state.turn)

        # aktuller Spieler
        print("Ich:", self.game_state.clone_current_player())

        # anderer Spieler und ein paar Wert
        noobPlayer = self.game_state.clone_other_player()
        print("Der Andere:", noobPlayer)
        print("Karotten:", noobPlayer.carrots, "| Karten:", noobPlayer.cards, "| Position:", noobPlayer.position)
        
        # das Spielfeld
        print("\n")
        print(self.game_state.board.track)
        
        

        # Zug zurückschicken
        return Move(action=Advance(distance=60, cards=[]))

    # this method is called every time the server has sent a new game state update
    # this method should be implemented to keep the game state up to date
    def on_update(self, state: GameState) -> None:
        
        # aktuelles GameState Objekt (state) wird in self.game_state gespeichert
        self.game_state = state

        ''' mein debug stuff, ist aber eig das gleiche wie oben
        poss = self.game_state.possible_moves();

        print("\n\n")
        print("turn:", self.game_state.turn)
        print(self.game_state.clone_current_player())
        print(self.game_state.clone_other_player())
        for p in poss:
            print(p)
        '''

if __name__ == "__main__":
    Starter(logic=Logic())
    # if u wanna have more insights, u can set the logging level to debug:
    # Starter(logic=Logic(), log_level=logging.DEBUG)