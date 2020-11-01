from game.Game import Game
from ai.Mcts_node import Mcts_node

import copy

class AI:
    def __init__(self, _visits):
        self.simulation_game = Game()
        self.visits = _visits

    def think(self, origin_game:Game):
        self.simulation_game = copy.deepcopy(origin_game)

        first_node = Mcts_node(self.simulation_game)

        for n in range(self.visits):
            self.simulation_game = copy.deepcopy(origin_game)

            first_node.game = self.simulation_game
            first_node.propagate()

        max_index = 0
        max_score = -1
        sum_visits = 0
        i = 0
        for node in first_node.next_node:
            node:Mcts_node
            score = 0
            if node.visits != 0:
                score = node.visits
            sum_visits+= node.visits
            print( node.visits, node.wins)
            if score > max_score:
                max_score = score
                max_index = i
            i+=1
        print("visits:", sum_visits)
        print("승률 :", first_node.next_node[max_index].wins / max_score)
        return first_node.next_pos[max_index]