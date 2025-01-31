import matrxies
import numpy
class points:
    def __init__(self,point_cords,origin = [0,0,0]):
        self.point_cords = point_cords
        self.origin = origin
    def return_points(self):
        return self.point_cords