import pygame
from game.Game import Game

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
b = 100
class gui:
    def __init__(self, _game:Game):
        self.size = (1000, 1000)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.game = _game
        self.pixel_size = 40
        pygame.display.set_caption("Gomoku_AI")
    def one_frame(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
        self.screen.fill(WHITE)
        #줄
        for i in range(self.game.board.size[1]):
            pygame.draw.line(self.screen, BLACK, (b, b + i * self.pixel_size),
                             (b + (self.game.board.size[0] - 1) * self.pixel_size, b + i * self.pixel_size))
        for i in range(self.game.board.size[0]):
            pygame.draw.line(self.screen, BLACK, (b + i * self.pixel_size, b),
                             (b + i * self.pixel_size, b + (self.game.board.size[1] - 1) * self.pixel_size))


        for i in range(self.game.board.size[1]):
            for j in range(self.game.board.size[0]):
                if self.game.board.board[i][j] == 1:
                    pygame.draw.circle(self.screen, BLACK, [b+j*self.pixel_size, b+i*self.pixel_size],
                                       int(self.pixel_size / 2))
                elif self.game.board.board[i][j] == 2:
                    pygame.draw.circle(self.screen, WHITE, [b + j * self.pixel_size, b + i * self.pixel_size],
                                       int(self.pixel_size / 2))
                    pygame.draw.circle(self.screen, BLACK, [b+j*self.pixel_size, b+i*self.pixel_size],
                                       int(self.pixel_size / 2), 2)
        pygame.display.flip()
