from DubinModel import DubinModel
'''
start, end p,o should be np array
if point is right of the segment o = 1, left of the segment o = 0
every 90 degree turn takes 6.3m path length (rho = 4)
'''


class DubinPathBetweenPoints:
    def __init__(self, startp, endp, starto, endo, Ts, v, rho):
        self.model = DubinModel(Ts, v, rho)
        self.normCoord = startp - endp
        self.x = []
        self.y = []
        self.rho = rho
        self.starto = starto
        self.endo = endo
        if starto == endo:
            self.sameo()
        else:
            self.differento()
        self.pathlength = 0
        f = open('90turns', 'rb')
        self.turn90coords = pickle.load(f)

    def sameo(self):
        if self.normCoord[1] < self.rho:
            # 2 270 degree turn
            self.pathlength = 6*6.3 + self.normCoord[1] + self.normCoord[0]
        else:
            # 2 90 degree turn
            self.pathlength = 2*6.3 + self.normCoord[1] - 8 + self.normCoord[0]

    def differento(self):
        # 4 90 degree turn
        self.pathlength = 4*6.3 + self.normCoord[0] + self.normCoord[1]

    def getPath(self):
        return self.x, self.y, self.pathlength
