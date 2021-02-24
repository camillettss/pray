from pyglet.gl import glRotated, glTranslated
from math import sin, cos, radians

class Player():
    def __init__(self, x, y, z, current_block) -> None:
        self.x, self.y, self.z = x, y, z
        self.angle_y = 0
        self.angle_x = 0
        self.vel_y = 0
        self.current_block = current_block
    
    def transform(self):
        glRotated(-self.angle_x, 1, 0, 0)
        glRotated(-self.angle_y, 0, 1, 0)
        glTranslated(-self.x, -self.y, -self.z)
    
    def apply_motion(self, _, amount, angle=0):
        #_ = self.x, self.y, self.z
        self.x -= sin(radians(self.angle_y+angle)) * amount
        self.z -= cos(radians(self.angle_y+angle)) * amount