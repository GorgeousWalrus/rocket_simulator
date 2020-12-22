class Engine:
  def __init__(self, height, radius, mass, max_thrust, max_fuel_consumption, fuel_ratio, min_throttle=0.6):
    self.height = height
    self.radius = radius
    self.max_thrust = max_thrust
    self.max_fuel_consumption = max_fuel_consumption
    self.mass = mass
    self.fuel_ratio = fuel_ratio
    self.min_throttle = min_throttle
    self.oxygen_tanks = []
    self.fuel_tanks = []
    self.throttle = 0

  def getFuel(self):
    total_oxygen = 0
    total_fuel = 0
    for tank in self.oxygen_tanks:
      total_oxygen += tank.fuel_mass
    for tank in self.fuel_tanks:
      total_fuel += tank.fuel_mass
    return total_fuel, total_oxygen
  
  def draw(self, consumption):
    # TODO: Properly empty the tanks in case of different amounts of fuel
    fuel_consumption = consumption / len(self.fuel_tanks)
    oxygen_consumption = consumption * self.fuel_ratio / len(self.oxygen_tanks)
    for tank in self.fuel_tanks:
      tank.draw(fuel_consumption)
    for tank in self.oxygen_tanks:
      tank.draw(oxygen_consumption)    

  def burn(self, t_step):
    if self.throttle < self.min_throttle:
      return
    fuel_consumption = self.throttle * self.max_fuel_consumption * t_step
    total_fuel, total_oxygen = self.getFuel()
    if (total_fuel >= fuel_consumption and
        total_oxygen >= fuel_consumption * self.fuel_ratio):
      self.draw(fuel_consumption)
      thrust = self.throttle * self.max_thrust
    else:
      thrust = 0
    return thrust

  def setThrottle(self, throttle):
    if throttle <= self.min_throttle/2:
      self.throttle = 0
    elif throttle <= self.min_throttle:
      self.throttle = self.min_throttle
    else:
      self.throttle = min(throttle, 1)