import os
from backend.rocket import Rocket
from backend.tank import Tank
from backend.engine import Engine
from backend.payload import Payload
import numpy 


oxygen = Tank(1, 0.2, 0.01, 1)
fuel = Tank(1, 0.2, 0.01, 0.5)
engine = Engine(0.5, 0.2, 0.02, 50, 0.1, 3)
payload = Payload(1, 1, 'cone')

rocket = Rocket(engine, [oxygen], [fuel], payload)
rocket.throttle(1)

t_step = 0.1

for t in numpy.arange(0, 100, t_step):
  rocket.burn(t_step)
  position = rocket.position[1]
  print(position)
  if position < 0:
    break