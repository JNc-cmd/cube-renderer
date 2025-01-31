import numpy
import matrxies
import points
class object:
    def __init__(self, vertices:numpy.matrix,object_orign:tuple[float,float,float] = (0,0,0,1),rotaion:tuple[float,float,float] = (0,0,0),xyz_cordz:tuple[float,float,float] = (0,0,0)):
        self.vertices = vertices
        self.object_orign = object_orign
        self.rotaion = rotaion
        self.xyz_cords = xyz_cordz
        self.vertices_points = []
        for point in self.vertices:
            self.vertices_points.append(points.points(point, object_orign))
        

    def update(self,step):
        self.points:list = []
        i = 0
        for func in self.vertices_points:
            self.points.append(self.vertices_points[i].translate(step[0],step[1],step[2]))
            i+=1
        s = numpy.matrix(numpy.array(self.points))
        return s
    def rotations(self,rot):
        self.points:list = []
        i = 0
        for func in self.vertices_points:
            
            self.points.append(self.vertices_points[i].zrotation(rot[2],(self.object_orign[0],self.object_orign[1],self.object_orign[2])))
            i+=1
        s = numpy.matrix(numpy.array(self.points))
        print(s)
        return s


