class Position:
  def __init__(self, x=0, y=0, z=0):
    self.x = x
    self.y = y
    self.z = z
    self.x_vel = 0
    self.y_vel = 0
    self.z_vel = 0
    self.length = 0
    self.x_norm = 0
    self.y_norm = 0
    self.z_norm = 0

  def update(self, t_step):
    self.x += self.x_vel * t_step
    self.y += self.y_vel * t_step
    self.z += self.z_vel * t_step
    self.norm()

  def printVelocity(self):
    print('x_vel:', self.x_vel, 'y_vel:', self.y_vel, 'z_vel:', self.z_vel, )
  
  def norm(self):
    self.length = abs(self.x_vel) + abs(self.y_vel) + abs(self.z_vel)
    if self.length == 0:
      return
    self.x_norm = self.x_vel / self.length
    self.y_norm = self.y_vel / self.length
    self.z_norm = self.z_vel / self.length
