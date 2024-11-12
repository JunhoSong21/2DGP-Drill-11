import game_framework
import title_mode
import item_mode
import pico2d
import game_world
from grass import *
from boy import *
from bird import *

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_mode(item_mode)
        else:
            if event.type == SDL_KEYDOWN or SDL_KEYUP:
                boy.add_event(event) # input 이벤트를 boy 에게 전달하고 있다.

def init():
    global running
    global grass
    global boy

    running = True

    grass = Grass() # 영속 객체
    game_world.add_object(grass, 0)

    boy = Boy() # 영속 객체
    game_world.add_object(boy, 1)

    bird = Bird()
    game_world.add_object(bird, 1)

def finish():
    game_world.clear()

def update():
    game_world.update_world()

def draw():
    pico2d.clear_canvas()
    game_world.render()
    pico2d.update_canvas()

def pause():
    pass

def resume():
    pass