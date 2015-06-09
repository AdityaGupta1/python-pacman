from tkinter import PhotoImage
from Sprite import Sprite
import time

class PacMan(Sprite):

    def __init__(self, game, photo_image):
        Sprite.__init__(self, game)
        self.game = game
        self.photo_image = photo_image
        # self.x = 240
        # self.y = 317
        self.x = 429
        self.y = 369
        game.canvas.bind_all("<KeyPress-Left>", self.left)
        game.canvas.bind_all("<KeyPress-Right>", self.right)
        game.canvas.bind_all("<KeyPress-Up>", self.up)
        game.canvas.bind_all("<KeyPress-Down>", self.down)
        self.image = game.canvas.create_image(self.x, self.y, image = self.photo_image, anchor = "sw")
        self.pacman_right = PhotoImage(file = "pacman-right.gif")
        self.pacman_left = PhotoImage(file = "pacman-left.gif")
        self.pacman_up = PhotoImage(file = "pacman-up.gif")
        self.pacman_down = PhotoImage(file = "pacman-down.gif")
        self.speed = 1
        self.direction = 0

    def goLeft(self, evt):
        self.x -= self.speed
        self.game.canvas.coords(self.image, self.x, self.y)
        self.game.canvas.itemconfig(self.image, image = self.pacman_left)

    def goRight(self, evt):
        self.x += self.speed
        self.game.canvas.coords(self.image, self.x, self.y)
        self.game.canvas.itemconfig(self.image, image = self.pacman_right)

    def goUp(self, evt):
        self.y -= self.speed
        self.game.canvas.coords(self.image, self.x, self.y)
        self.game.canvas.itemconfig(self.image, image = self.pacman_up)

    def goDown(self, evt):
        self.y += self.speed
        self.game.canvas.coords(self.image, self.x, self.y)
        self.game.canvas.itemconfig(self.image, image = self.pacman_down)

    def move(self):
        if self.direction == 1:
            self.goUp(self)
        elif self.direction == 2:
            self.goRight(self)
        elif self.direction == 3:
            self.goDown(self)
        elif self.direction == 4:
            self.goLeft(self)

    def up(self, evt):
        self.direction = 1

    def right(self, evt):
        self.direction = 2

    def down(self, evt):
        self.direction = 3

    def left(self, evt):
        self.direction = 4

