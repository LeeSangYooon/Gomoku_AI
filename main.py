from game.Game import Game
from ai.AI import AI
from gui.gui import gui
game = Game()
gui = gui(game)

while True:
    pos = (int(input("x : ")), int(input("y : ")))
    game.move(pos)
    gui.one_frame()
    if game.result != 0:
        print (str(game.result) + " 이/가 이겼습니다!")

    aimove =AI(1500).think(game)
    game.move(aimove)

    gui.one_frame()
    if game.result != 0:
        print (str(game.result) + " 이/가 이겼습니다!")