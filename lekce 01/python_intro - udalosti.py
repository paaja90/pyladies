import pyglet
window = pyglet.window.Window()

label = pyglet.text.Label('Ahoj!', x=10, y=30)

@window.event
def on_text(text):
    existujici_text = label.text
    label.text = existujici_text + text

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
print('Hotovo!')
