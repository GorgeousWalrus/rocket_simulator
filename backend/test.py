from rocket import Rocket
from tank import Tank
from engine import Engine
from payload import Payload
import numpy 

oxygen = Tank(1, 0.2, 0.01, 6)
fuel = Tank(1, 0.2, 0.01, 2)
engine = Engine(0.5, 0.2, 0.02, 100, 0.1, 3)
payload = Payload(1, 1, 'cone')

rocket = Rocket(engine, [oxygen], [fuel], payload)
rocket.throttle(1)

t_step = 0.1

for t in numpy.arange(0, 100, t_step):
  rocket.burn(t_step)
  print(rocket.position[2])