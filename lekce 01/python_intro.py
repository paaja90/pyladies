import pyglet
from random import randrange
window = pyglet.window.Window()

green_image = pyglet.image.load('green.png')
apple_image = pyglet.image.load('apple.png')

snake_tiles = {}
for start in ['bottom','top','end','left','right']:
    for end in ['bottom','top','end','left','right','tongue','dead']:
        key = start + '-' + end
        image = pyglet.image.load('snake-tiles/' + key + '.png')
        snake_tiles[key] = image

def direction(a, b):
    if b == 'end':
        return 'end'
    a_x, a_y = a
    b_x, b_y = b
    if a_x == b_x + 1:
        return 'left'
    elif a_x == b_x - 1:
        return 'right'
    elif a_y == b_y + 1:
        return 'bottom'
    elif a_y == b_y - 1:
        return 'top'
    else:
        return 'end'

print(snake_tiles)



class GameState:
    def initialize(self):
        self.snake = [(1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5)]
        self.food = [(2, 0), (5, 1), (1, 4)]
        self.direction = 1,0
        self.alive = True

    def draw(self):
        prevs = ['end'] + self.snake[:-1]
        nexts = self.snake[1:] + ['end']
        for coordinates, prev, next in zip(self.snake, prevs, nexts):
            before = direction(coordinates, prev)
            after = direction(coordinates, next)
            if after == 'end' and not self.alive:
                after = 'dead'
            key = before + '-' + after
            x, y = coordinates
            image = snake_tiles[key]
            image.blit(x*tile_size, y*tile_size, width=tile_size, height=tile_size)
        for x, y in self.food:
            apple_image.blit(x*tile_size, y*tile_size, width=tile_size, height=tile_size)

    def move(self, t):
        if not self.alive:
            return
        x, y = self.snake[-1]
        direction_x, direction_y = self.direction
        new_x = x + direction_x
        new_y = y + direction_y
        new_head = new_x, new_y
        if new_head in self.snake:
            self.alive = False
        if new_x < 0:
            self.alive = False
        if new_y < 0:
            self.alive = False
        if new_x >= window.width//tile_size:
            self.alive = False
        if new_y >= window.height//tile_size:
            self.alive = False
        self.snake.append(new_head)
        if new_head in self.food:
            self.food.remove(new_head)
            self.add_food()
        else:
            del self.snake[0]

    def add_food(self):
        for n in range(100):
            x = randrange(window.width//tile_size)
            y = randrange(window.height//tile_size)
            new_food = x,y
            if new_food not in self.snake and new_food not in self.food:
                self.food.append(new_food)
                return



state = GameState()
state.initialize()
print(state.snake)


pyglet.clock.schedule_interval(state.move, 1/4)

label = pyglet.text.Label('Ahoj!', x=10, y=30)

tile_size = 55

@window.event
def on_draw():
      # Lepší vykreslování (pro nás zatím kouzelné zaříkadlo)
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
    window.clear()
    state.draw()
    label.draw()

@window.event
def on_key_press(key_code, modifier):
    if key_code == pyglet.window.key.LEFT:
        state.direction = -1,0
    elif key_code == pyglet.window.key.RIGHT:
        state.direction = 1,0
    elif key_code == pyglet.window.key.DOWN:
        state.direction = 0,-1
    elif key_code == pyglet.window.key.UP:
        state.direction = 0,1

pyglet.app.run()
print('Hotovo!')
