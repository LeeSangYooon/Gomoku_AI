import numpy
class Board:
    def __init__(self):
        self.size = (9, 9)
        self.board = numpy.zeros((self.size[0], self.size[1]), dtype=int)