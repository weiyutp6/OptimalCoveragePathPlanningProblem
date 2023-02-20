import numpy as np
'''
Ts is sample time
v is constant velocity
rho is turning radius
u is normalized control input between -1 and 1
'''


class DubinModel:
    def __init__(self, Ts, v, rho):
        self.x = 0
        self.y = 0
        self.theta = 0
        self.Ts = Ts
        self.xdot = 0
        self.ydot = 0
        self.thetadot = 0
        self.v = v
        self.rho = rho

    def update(self, u):
        self.x += self.xdot * self.Ts
        self.y += self.ydot * self.Ts
        self.theta += self.thetadot * self.Ts
        self.xdot = self.v * np.cos(self.theta)
        self.ydot = self.v * np.sin(self.theta)
        self.thetadot = u / self.rho
        return self.x, self.y
