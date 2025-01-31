import points
class triangle:
    def __init__(self,points:list[points.points,points.points,points.points]):
        self.points = points
    def __getitem__(self, key):
        return self.points[key]