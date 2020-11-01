from game.Board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 1
        self.result = 0

    def move(self, pos):
        self.board.board[pos[1]][pos[0]] = self.turn
        self.result = self.get_result(pos)
        self.turn = 3 - self.turn

    def get_result(self, pos):
        x = pos[0]
        y = pos[1]
        row = 0
        for i in range(self.board.size[0]):
            if self.board.board[y][i] == self.turn:
                row += 1
                if row == 5:
                    return self.turn
            else:
                row = 0
        row = 0
        for i in range(self.board.size[1]):
            if self.board.board[i][x] == self.turn:
                row += 1
                if row == 5:
                    return self.turn
            else:
                row = 0
        row = 0
        min_pos = min(x, y)
        i = y - min_pos
        j = x - min_pos
        while j<self.board.size[0] and i<self.board.size[1]:
            if self.board.board[i][j] == self.turn:
                row += 1
                if row == 5:
                    return self.turn
            else:
                row = 0
            i+=1
            j+=1
        i = y - min_pos
        j = self.board.size[0] - x + min_pos - 1

        while j>=0 and i<self.board.size[1]:
            if self.board.board[i][j] == self.turn:
                row += 1
                if row == 5:
                    return self.turn
            else:
                row = 0
            i+=1
            j-=1
        return 0