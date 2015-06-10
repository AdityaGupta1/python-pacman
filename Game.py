from tkinter import *
import random as seed
import time

class Game:

    def __init__(self):
        self.root = Tk()
        self.text = Text(self.root, height = 1, width = 50)
        self.text.pack()
        self.text.insert(END, "Use the arrow keys to control PacMan!")
        self.root.lift(aboveThis=None)
        self.root.bind('<KeyPress-Up>', self.moveUp)
        self.root.bind('<KeyPress-Right>', self.moveRight)
        self.root.bind('<KeyPress-Left>', self.moveLeft)
        self.root.bind('<KeyPress-Down>', self.moveDown)
        self.board = \
        ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■",
         "■", "G", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "G", "■",
         "■", "◦", "■", "◦", "■", "◦", "■", "◦", "■", "◦", "■", "◦", "■", "◦", "■",
         "■", "◦", "■", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "■", "◦", "■",
         "■", "◦", "■", "◦", "■", "◦", "■", "◦", "■", "◦", "■", "◦", "■", "◦", "■",
         "■", "◦", "■", "◦", "■", "◦", "■", "P", "■", "◦", "■", "◦", "■", "◦", "■",
         "■", "◦", "◦", "◦", "■", "◦", "■", "◦", "■", "◦", "■", "◦", "◦", "◦", "■",
         "■", "◦", "■", "◦", "■", "◦", "◦", "◦", "◦", "◦", "■", "◦", "■", "◦", "■",
         "■", "◦", "■", "◦", "■", "■", "■", "◦", "■", "■", "■", "◦", "■", "◦", "■",
         "■", "G", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "◦", "G", "■",
         "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]
        self.map_width = 15
        self.map_height = 11
        self.pacman_pos = 82
        self.ghost1_pos = 16
        self.ghost2_pos = 28
        self.ghost3_pos = 136
        self.ghost4_pos = 148
        self.score = 0
        self.wall = "■"
        self.pellet = "◦"
        self.pacman = "P"
        self.ghost = "G"
        self.empty = " "
        self.g1p = True
        self.g2p = True
        self.g3p = True
        self.g4p = True
        self.game_over = False

    def moveGhosts(self):
        self.moveGhost(1)
        self.moveGhost(2)
        self.moveGhost(3)
        self.moveGhost(4)

    def getRandomPos(self):
        random = seed.randint(1, 4)
        direction = 0
        if random == 1:
            direction = 1
        elif random == 2:
            direction = -1
        elif random == 3:
            direction = self.map_width
        elif random == 4:
            direction = -self.map_width
        return direction

    def moveGhost(self, ghost):
        temp2 = 0
        temp3 = 0
        if ghost == 1:
            temp2 = self.ghost1_pos
            temp3 = self.g1p
        elif ghost == 2:
            temp2 = self.ghost2_pos
            temp3 = self.g2p
        elif ghost == 3:
            temp2 = self.ghost3_pos
            temp3 = self.g3p
        elif ghost == 4:
            temp2 = self.ghost4_pos
            temp3 = self.g4p
        temp = False
        while temp == False:
            direction = self.getRandomPos()
            if not self.board[temp2 + direction] == self.wall:
                if self.board[temp2 + direction] == self.pellet:
                    g1p = True
                else:
                    g1p = False

                if self.board[temp2 + direction] == self.pacman:
                    self.gameOver()

                self.board[temp2 + direction] = self.ghost

                if g1p:
                    self.board[temp2] = self.pellet
                else:
                    self.board[temp2] = self.empty
                temp2 += direction
                self.board[temp2] = self.ghost
                temp = True
            else:
                temp = False

        if ghost == 1:
            self.ghost1_pos = temp2
            self.g1p = temp3
        elif ghost == 2:
            self.ghost2_pos = temp2
            self.g2p = temp3
        elif ghost == 3:
            self.ghost3_pos = temp2
            self.g3p = temp3
        elif ghost == 4:
            self.ghost4_pos = temp2
            self.g4p = temp3

    def printMap(self, ghosts):
        if ghosts == True:
            self.moveGhosts()
        for x in range(0, self.map_height):
            temp2 = ""
            for y in range(0, self.map_width):
                temp = (self.map_width * x)
                temp2 = temp2 + self.board[temp + y] + " "
            print(temp2)
        print("Score: " + str(self.score))

    def move(self, direction):
        if not self.board[self.pacman_pos + direction] == self.wall and self.game_over == False:
            if self.board[self.pacman_pos + direction] == self.pellet:
                self.score += 10
            self.board[self.pacman_pos] = self.empty
            self.pacman_pos += direction
            self.board[self.pacman_pos] = self.pacman
            self.printMap(True)

    def moveUp(self, evt):
        self.move(-self.map_width)

    def moveRight(self, evt):
        self.move(1)

    def moveDown(self, evt):
        self.move(self.map_width)

    def moveLeft(self, evt):
        self.move(-1)

    def gameOver(self):
        self.game_over = True


game = Game()
game.printMap(game)
while True:
    game.root.update()
    game.root.update_idletasks()