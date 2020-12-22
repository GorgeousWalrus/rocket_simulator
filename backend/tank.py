class Tank:
  def __init__(self, height, radius, empty_mass, fuel_mass):
    self.height = height
    self.radius = radius
    self.empty_mass = empty_mass
    self.fuel_mass = fuel_mass
    self.current_mass = empty_mass + fuel_mass
    self.COM = (0, 0, height/2)

  def draw(self, mass):
    if self.fuel_mass < mass:
      raise Exception('Not enough Fuel')
    self.fuel_mass -= mass