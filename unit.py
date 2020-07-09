class Unit(self):
    #rank
    def __init__(self,a,h,c,m,r):
        self.combat = a
        self.health = h
        self.cost = c
        self.move = m
        self.range = r

infantry = Unit(2,1,3,2,1)
motor_inf = Unit(4,1,5,5,1)
tank = Unit(6,2,8,4,3)
artillery = Unit(7,1,8,1,6)

transport = Unit(0,1,4,3,0)
battleship = Unit(7,2,14,2,6)
fac = Unit(2,1,4,6,1)
submarine = Unit(4,1,8,3,2)