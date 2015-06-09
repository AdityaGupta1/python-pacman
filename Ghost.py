from Sprite import Sprite

class Ghost(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image = self.photo_image, anchor = "sw")
        self.coordinates = (x, y, x + width, y + height)