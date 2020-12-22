import pyglet
from pyglet import shapes
from pyglet.window import key
from pyglet.gl import *

# backend
from backend.rocket import Rocket
from backend.tank import Tank
from backend.engine import Engine
from backend.payload import Payload
import numpy

oxygen = Tank(1, 0.2, 0.01, 1)
fuel = Tank(1, 0.2, 0.01, 0.5)
engine = Engine(0.5, 0.2, 0.02, 30, 0.1, 3)
payload = Payload(1, 1, 'cone')

rocket = Rocket(engine, [oxygen], [fuel], payload)
rocket.throttle(1)

def movement():
  if keys[key.DOWN]:
    glTranslatef(0,10,0)
  if keys[key.UP]:
    glTranslatef(0,-10,0)
  if keys[key.RIGHT]:
    glTranslatef(-10,0,0)
  if keys[key.LEFT]:
    glTranslatef(10,0,0)
  if keys[key.N]:
    glScalef(0.9, 0.9, 0.9)
  if keys[key.M]:
    glScalef(1.1, 1.1, 1.1)

keys = key.KeyStateHandler()
window = pyglet.window.Window(width=640, height=480)
window.push_handlers(keys)
glClearColor(0.71, 0.90, 0.92, 1)
batch = pyglet.graphics.Batch()
square = shapes.Rectangle(-1000, 0, 2000, 200, color=(63, 138, 56), batch=batch)

glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
rocket_height = 100 # rocket height in cm
rocket_front = pyglet.image.load('sprites/rocket.png')
rocket_front = pyglet.sprite.Sprite(rocket_front, x=200, y=200, batch=batch)
rocket_front.scale = rocket_height / rocket_front.height

prev_x, prev_y = 0, 0
def update(dt):
    window.clear()
    batch.draw()
    movement()
    rocket_front.y = 200 + int(rocket.position[1]*10)
    print(rocket.position[1])
    rocket.burn(dt)

pyglet.clock.schedule_interval(update,1/60)
pyglet.app.run()
