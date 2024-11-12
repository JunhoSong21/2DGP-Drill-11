import game_framework
import pico2d
import logo_mode as start_mode # logo_mode를 import 하지만 이름을 start_mode로 변경한다.

pico2d.open_canvas()
game_framework.run(start_mode)
pico2d.close_canvas()