import numpy
class Board:
    def __init__(self):
        self.size = (15, 15)
        self.board = numpy.zeros((self.size[0], self.size[1]), dtype=int)