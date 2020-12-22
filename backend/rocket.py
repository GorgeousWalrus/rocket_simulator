from .engine import Engine
from .tank import Tank
from .payload import Payload
from .position import Position
import random

class Rocket:
  G = 9.81
  x_sheer = random.randint(-20, 20) / 10
  z_sheer = random.randint(-20, 20) / 10

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
    self.position = Position()
    self.direction = Position()
    self.direction.y_norm = 1
    self.engine.oxygen_tanks = oxygen_tanks
    self.engine.fuel_tanks = fuel_tanks

  def update(self, t_step):
    self.current_mass = self.empty_mass
    for tank in self.oxygen_tanks + self.fuel_tanks:
      self.current_mass += tank.fuel_mass
    self.position.update(t_step)

  def burn(self, t_step):
    thrust = self.engine.burn(t_step)
    gimbal = self.engine.gimbal(self.position, self.direction)
    x_accel = thrust * gimbal[0] / self.current_mass + self.x_sheer
    y_accel = thrust * gimbal[1] / self.current_mass - self.G
    z_accel = thrust * gimbal[2] / self.current_mass + self.z_sheer
    self.position.x_vel += x_accel*t_step
    self.position.y_vel += y_accel*t_step
    self.position.z_vel += z_accel*t_step
    self.update(t_step)

  def throttle(self, throttle):
    self.engine.setThrottle(throttle)

  def printVelocity(self):
    self.position.printVelocity()