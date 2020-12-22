from engine import Engine
from tank import Tank
from payload import Payload

class Rocket:

  G = 9.81

  def __init__(self, engine, oxygen_tanks, fuel_tanks, payload):
    self.engine = engine
    self.oxygen_tanks = oxygen_tanks
    self.fuel_tanks = fuel_tanks
    self.payload = payload
    self.empty_mass = engine.mass + payload.mass
    self.current_mass = 0
    self.height = engine.height + payload.height
    for tank in oxygen_tanks + fuel_tanks:
      self.empty_mass += tank.empty_mass
      self.current_mass += tank.fuel_mass
      self.height += tank.height
    self.COM = self.height / 2
    self.pos_delta = [0, 0, 0]
    self.position = [0, 0, 0]
    self.velocity = 0
    self.engine.oxygen_tanks = oxygen_tanks
    self.engine.fuel_tanks = fuel_tanks

  def update(self, t_step):
    self.current_mass = self.empty_mass
    for tank in self.oxygen_tanks + self.fuel_tanks:
      self.current_mass += tank.fuel_mass
    self.pos_delta[1] = self.velocity * t_step
    self.position[1] += self.pos_delta[1]

  def burn(self, t_step):
    thrust = self.engine.burn(t_step)
    acceleration = thrust / self.current_mass - self.G
    self.velocity += acceleration*t_step
    self.update(t_step)
    
  def throttle(self, throttle):
    self.engine.setThrottle(throttle)