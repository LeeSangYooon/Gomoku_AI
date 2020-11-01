from game.Game import Game
from random import uniform, randint


class Mcts_node:
    def __init__(self, _simulation_game: Game):
        self.len_of_next = 0
        self.next_node = []
        self.next_pos = []
        self.visits = 0
        self.wins = 0
        self.game = _simulation_game
        self.my_turn = 0

    def get_moves(self):
        moves = set()
        for i in range(self.game.board.size[1]):
            for j in range(self.game.board.size[0]):
                if self.game.board.board[i][j] != 0:
                    poses = [(j - 1, i - 1), (j - 1, i), (j - 1, i + 1), (j, i - 1), (j, i + 1), (j + 1, i - 1),
                             (j + 1, i),
                             (j + 1, i + 1)]
                    for pos in poses:
                        if pos[0] >= 0 and pos[0] < self.game.board.size[0] and pos[1] >= 0 and pos[
                            1] < self.game.board.size[1] and self.game.board.board[pos[1]][pos[0]] == 0:
                            moves.add(pos)
        return list(moves)

    def propagate(self):
        if self.visits == 0:  # 처음 오는 노드일 때
            self.next_pos = self.get_moves()
            self.len_of_next = len(self.next_pos)
            if self.len_of_next == 0:  # 이동할수 없으면 종료
                return 0
            self.next_node = [Mcts_node(self.game) for _ in range(self.len_of_next)]

            self.my_turn = self.game.turn

        max_index = 0
        max_score = -1
        i = 0
        for node in self.next_node:
            node: Mcts_node
            score = (node.wins + uniform(0.01, 0.85)) / (node.visits + 0.01) * uniform(0.5,0.7)
            if max_score < score:
                max_score = score
                max_index = i
            i += 1

        self.game.move(self.next_pos[max_index])

        if self.game.result != 0:
            self.visits += 1
            return self.game.result

        self.next_node[max_index].game = self.game
        result = self.next_node[max_index].propagate()
        if result != self.my_turn:
            self.wins += 1
        self.visits += 1

        return result
