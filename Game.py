from tkinter import *
import random
import time
from Ghost import Ghost
from PacMan import PacMan


class Game:

    def __init__(self):
        self.tk = Tk()
        self.tk.title("PacMan in Python")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width = 500, height = 500)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.bg = PhotoImage(file = "background.gif")
        self.canvas.create_image(0, 500, image = self.bg, anchor = "sw")
        self.sprites = []
        self.moving = False
        self.pacman = PacMan(self, PhotoImage(file = "pacman-start.gif"))
        self.sprites.append(self.pacman)

    def loop(self):
        while True:
            self.tk.update_idletasks()
            self.tk.update()
            self.pacman.move()
            time.sleep(0.01)

g = Game()
blinky = Ghost(g, PhotoImage(file = "ghost1.gif"), 200, 200, 20, 20)
g.sprites.append(blinky)
clyde = Ghost(g, PhotoImage(file = "ghost2.gif"), 200, 200, 20, 20)
g.sprites.append(clyde)
inky = Ghost(g, PhotoImage(file = "ghost3.gif"), 200, 200, 20, 20)
g.sprites.append(inky)
pinky = Ghost(g, PhotoImage(file = "ghost4.gif"), 200, 200, 20, 20)
g.sprites.append(pinky)
g.loop()