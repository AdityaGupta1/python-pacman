from tkinter import *
import random as seed

class Game:

    def __init__(self):
        self.root = Tk()
        self.text = Text(self.root, height = 1, width = 50)
        self.text.pack()
        self.text.insert(END, "Use the arrow keys to control PacMan!")
        self.root.bind('<KeyPress-Up>', self.moveUp)
        self.root.bind('<KeyPress-Right>', self.moveRight)
        self.root.bind('<KeyPress-Left>', self.moveLeft)
        self.root.bind('<KeyPress-Down>', self.moveDown)
        self.board = \
        ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■",
         "■", "G", "◦", "◦", "◦", "◦", "◦", "◦", "G", "■",
         "■", "◦", "■", "■", " ", "◦", "■", "■", "◦", "■",
         "■", "◦", "■", "■", "◦", " ", "■", "■", "◦", "■",
         "■", "◦", "■", "◦", "P", "◦", "◦", "■", "◦", "■",
         "■", "◦", " ", " ", "■", "■", " ", " ", "◦", "■",
         "■", "◦", "■", "◦", "◦", " ", "◦", "■", "◦", "■",
         "■", "◦", "■", "■", " ", "◦", "■", "■", "◦", "■",
         "■", "G", "◦", "◦", "◦", "◦", "◦", "◦", "G", "■",
         "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]
        self.pacman_pos = 44
        self.ghost1_pos = 11
        self.ghost2_pos = 18
        self.ghost3_pos = 81
        self.ghost4_pos = 88
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

    def moveGhosts(self):
        self.moveGhost1()
        self.moveGhost2()
        self.moveGhost3()
        self.moveGhost4()

    def getRandomPos(self):
        random = seed.randint(1, 4)
        temp = 0
        if random == 1:
            temp = 1
        elif random == 2:
            temp = -1
        elif random == 3:
            temp = 10
        elif random == 4:   
            temp = -10
        return temp


    def moveGhost1(self):
        temp = False
        direction = 0
        while temp == False:
            direction = self.getRandomPos()
            if not self.board[self.ghost1_pos + direction] == self.wall:
                if self.board[self.ghost1_pos + direction] == self.pellet:
                    g1p = True
                else:
                    g1p = False

                if self.board[self.ghost1_pos + direction] == self.pacman:
                     self.gameOver()

                if g1p == True:
                    self.board[self.ghost1_pos] = self.pellet
                else:
                    self.board[self.ghost1_pos] = self.empty
                self.ghost1_pos += direction
                self.board[self.ghost1_pos] = self.ghost
                temp = True
            else:
                temp = False

    def moveGhost2(self):
        temp = False
        direction = 0
        while temp == False:
            direction = self.getRandomPos()
            if not self.board[self.ghost2_pos + direction] == self.wall:
                if self.board[self.ghost2_pos + direction] == self.pellet:
                    g1p = True
                else:
                    g1p = False

                if self.board[self.ghost2_pos + direction] == self.pacman:
                     self.gameOver()

                if g1p == True:
                    self.board[self.ghost2_pos] = self.pellet
                else:
                    self.board[self.ghost2_pos] = self.empty
                self.ghost2_pos += direction
                self.board[self.ghost2_pos] = self.ghost
                temp = True
            else:
                temp = False

    def moveGhost3(self):
        temp = False
        direction = 0
        while temp == False:
            direction = self.getRandomPos()
            if not self.board[self.ghost3_pos + direction] == self.wall:
                if self.board[self.ghost3_pos + direction] == self.pellet:
                    g1p = True
                else:
                    g1p = False

                if self.board[self.ghost3_pos + direction] == self.pacman:
                     self.gameOver()

                if g1p == True:
                    self.board[self.ghost3_pos] = self.pellet
                else:
                    self.board[self.ghost3_pos] = self.empty
                self.ghost3_pos += direction
                self.board[self.ghost3_pos] = self.ghost
                temp = True
            else:
                temp = False

    def moveGhost4(self):
        temp = False
        direction = 0
        while temp == False:
            direction = self.getRandomPos()
            if not self.board[self.ghost4_pos + direction] == self.wall:
                if self.board[self.ghost4_pos + direction] == self.pellet:
                    g1p = True
                else:
                    g1p = False

                if self.board[self.ghost4_pos + direction] == self.pacman:
                     self.gameOver()

                if g1p == True:
                    self.board[self.ghost4_pos] = self.pellet
                else:
                    self.board[self.ghost4_pos] = self.empty
                self.ghost4_pos += direction
                self.board[self.ghost4_pos] = self.ghost
                temp = True
            else:
                temp = False



    def printMap(self, *args):
        self.moveGhosts()
        for x in range(0, 10):
            temp = (10 * x)
            print(self.board[temp] + " " + self.board[temp + 1] + " " + self.board[temp + 2] + " " + self.board[temp + 3] + " " + self.board[temp + 4] + " " + self.board[temp + 5] + " " + self.board[temp + 6] + " " + self.board[temp + 7] + " " + self.board[temp + 8] + " " + self.board[temp + 9] + " ")
        print("Score: " + str(self.score))

    def printMapWithGhosts(self, *args):
        self.moveGhosts()
        for x in range(0, 10):
            temp = (10 * x)
            print(self.board[temp] + " " + self.board[temp + 1] + " " + self.board[temp + 2] + " " + self.board[temp + 3] + " " + self.board[temp + 4] + " " + self.board[temp + 5] + " " + self.board[temp + 6] + " " + self.board[temp + 7] + " " + self.board[temp + 8] + " " + self.board[temp + 9] + " ")
        print("Score: " + str(self.score))
        self.moveGhosts()

    def moveUp(self, evt):
        if not self.board[self.pacman_pos - 10] == self.wall:
            if self.board[self.pacman_pos - 10] == self.pellet:
                self.score += 10
            self.board[self.pacman_pos] = self.empty
            self.pacman_pos -= 10
            self.board[self.pacman_pos] = self.pacman
            self.printMapWithGhosts()

    def moveRight(self, evt):
        if not self.board[self.pacman_pos + 1] == self.wall:
            if self.board[self.pacman_pos + 1] == self.pellet:
                self.score += 10
            self.board[self.pacman_pos] = self.empty
            self.pacman_pos += 1
            self.board[self.pacman_pos] = self.pacman
            self.printMapWithGhosts()

    def moveDown(self, evt):
        if not self.board[self.pacman_pos + 10] == self.wall:
            if self.board[self.pacman_pos + 10] == self.pellet:
                self.score += 10
            self.board[self.pacman_pos] = self.empty
            self.pacman_pos += 10
            self.board[self.pacman_pos] = self.pacman
            self.printMapWithGhosts()

    def moveLeft(self, evt):
        if not self.board[self.pacman_pos - 1] == self.wall:
            if self.board[self.pacman_pos - 1] == self.pellet:
                self.score += 10
            self.board[self.pacman_pos] = self.empty
            self.pacman_pos -= 1
            self.board[self.pacman_pos] = self.pacman
            self.printMapWithGhosts()

    def gameOver(self):
        pass

game = Game()
game.printMap(game)
while True:
    game.root.update()
    game.root.update_idletasks()