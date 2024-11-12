import game_framework
import title_mode
import play_mode
import game_world
import pico2d
from pannel import *

def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel, 3)

def finish():
    game_world.remove_object(pannel)

def update():
    pass

def handle_events():
    events = pico2d.get_events()

    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            game_framework.pop_mode()
        elif event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_0:
            play_mode.boy.set_item('NONE')
            game_framework.pop_mode()
        elif event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_1:
            play_mode.boy.set_item('SmallBall')
            game_framework.pop_mode()
        elif event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_2:
            play_mode.boy.set_item('BigBall')
            game_framework.pop_mode()

def draw():
    pico2d.clear_canvas()
    game_world.render()
    pico2d.update_canvas()

def pause():
    pass

def resume():
    pass