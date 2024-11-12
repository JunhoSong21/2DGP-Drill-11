import pico2d

class Grass:
    def __init__(self):
        self.image = pico2d.load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass