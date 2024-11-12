import game_framework
import title_mode
import play_mode
import pico2d

def init():
    global image
    image = pico2d.load_image('title.png')

def finish():
    global image
    del image

def update():
    pass

def handle_events():
    events = pico2d.get_events()

    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif (event.type, event.key) == (pico2d.SDL_KEYDOWN, pico2d.SDLK_SPACE):
            game_framework.change_mode(play_mode)

def draw():
    pico2d.clear_canvas()
    image.draw(400, 300)
    pico2d.update_canvas()

def pause():
    pass

def resume():
    pass