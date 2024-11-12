import game_framework
import title_mode
import pico2d

def init():
    global image
    global logo_start_time

    image = pico2d.load_image('tuk_credit.png')
    logo_start_time = pico2d.get_time()

def finish():
    global image
    del image

def update():
    global logo_start_time

    if pico2d.get_time() - logo_start_time >= 2.0:
        logo_start_time = pico2d.get_time()
        game_framework.change_mode(title_mode)

def draw():
    pico2d.clear_canvas()
    image.draw(400, 300)
    pico2d.update_canvas()

def handle_events():
    events = pico2d.get_events()

def pause():
    pass

def resume():
    pass