# world[0] : 백그라운드 객체들. 맨 아래에 그려야 할 객체들
# world[1] : 포어그라운드 객체들. 위에 그려야 할 객체들
world = [[] for _ in range(4)]

def add_object(o, depth):
    world[depth].append(o)

def update_world():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return # 지우는데 성공했다면 리턴
    
    print('ERROR: Not Exist Object cannot remove')

def clear():
    for layer in world:
        layer.clear()