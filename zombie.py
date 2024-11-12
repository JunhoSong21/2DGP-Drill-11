import random
import math
import game_framework
import game_world

from pico2d import *

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

animation_names = ['Walk']

class Zombie:
    images = None

    def load_images(self):
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombie/"+ name + " (%d)" % i + ".png") for i in range(1, 11)]

    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = random.randint(1600-800, 1600), 150
        self.load_images()
        self.frame = random.randint(0, 9)
        self.dir = random.choice([-1,1])
        self.life = 2

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 1600:
            self.dir = -1
        elif self.x < 800:
            self.dir = 1
        self.x = clamp(800, self.x, 1600)

        

    def draw(self):
        if self.life == 2:
            draw_rectangle(*self.get_bb())
            self.font.draw(self.x-10, self.y + 100, f'{self.life:02d}', (0, 0, 255))
            if self.dir < 0:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 200, 200)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 200, 200)
        elif self.life == 1:
            draw_rectangle(*self.get_bb())
            self.font.draw(self.x-10, self.y + 100, f'{self.life:02d}', (0, 0, 255))
            if self.dir < 0:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y - 35, 130, 130)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y - 35, 130, 130)

    def handle_event(self, event):
        pass

    def get_bb(self):
        if self.life == 2: return self.x - 60, self.y - 90, self.x + 60, self.y + 90
        elif self.life == 1: return self.x - 50, self.y - 90, self.x + 50, self.y + 30
    
    def handle_collision(self, group, other):
        if group == 'boy:zombie':
            pass
        elif group == 'ball:zombie':
            self.life -= 1

        if self.life <= 0:
            game_world.remove_object(self)