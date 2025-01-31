import triangle
import numpy
import matrxies
import points
class mesh:
    def __init__(self,triangles:list[triangle.triangle]):
        self.triangles = triangles
    def translate(self,tx,ty,tz):
        for t in self.triangles:
            p1 = t.points
            for s in range(0,2):
                a = numpy.matrix(p1[0].return_points())
                b = numpy.matrix(p1[1].return_points())
                c = numpy.matrix(p1[2].return_points())
                a= numpy.c_[a,[1]]
                b= numpy.c_[b,[1]]
                c= numpy.c_[c,[1]]
                c1=matrxies.translation(tx,ty,tz,a)
                c2=matrxies.translation(tx,ty,tz,b)
                c3=matrxies.translation(tx,ty,tz,c)
                
                a = c1.tolist()
                b = c2.tolist()
                c = c3.tolist()
                A_postion_list = [a[0][0]+a[0][3], a[1][1]+a[1][3], a[2][0] + a[2][3]] 
                B_postion_list = [b[0][0]+b[0][3], b[1][1]+b[1][3], b[2][0] + b[2][3]]
                C_postion_list = [c[0][0]+c[0][3], c[1][1]+c[1][3], c[2][0] + c[2][3]]          
                t.points = [points.points(A_postion_list),points.points(B_postion_list),points.points(C_postion_list)]
    def scale(self):
        pass
    def rotate_z(self,rot):
        for t in self.triangles:
            p1 = t.points
            for s in range(0,2):
                a = numpy.matrix(p1[0].return_points())
                b = numpy.matrix(p1[1].return_points())
                c = numpy.matrix(p1[2].return_points())
                a= numpy.c_[a,[1]]
                b= numpy.c_[b,[1]]
                c= numpy.c_[c,[1]]
                c1=matrxies.zrot(numpy.deg2rad(rot),a)
                c2=matrxies.zrot(numpy.deg2rad(rot),b)
                c3=matrxies.zrot(numpy.deg2rad(rot),c)
                
                a = c1.tolist()
                b = c2.tolist()
                c = c3.tolist()
                A_postion_list = [a[0][0]+a[0][1], a[1][0]+a[1][1], a[2][2]] 
                B_postion_list = [b[0][0]+b[0][1], b[1][0]+b[1][1], b[2][2]]
                C_postion_list = [c[0][0]+c[0][1], c[1][0]+c[1][1], c[2][2]]          
                t.points = [points.points(A_postion_list),points.points(B_postion_list),points.points(C_postion_list)]
    def rotate_y(self,rot):
        for t in self.triangles:
            p1 = t.points
            for s in range(0,2):
                a = numpy.matrix(p1[0].return_points())
                b = numpy.matrix(p1[1].return_points())
                c = numpy.matrix(p1[2].return_points())
                a= numpy.c_[a,[1]]
                b= numpy.c_[b,[1]]
                c= numpy.c_[c,[1]]
                c1=matrxies.y_rot(numpy.deg2rad(rot),a)
                c2=matrxies.y_rot(numpy.deg2rad(rot),b)
                c3=matrxies.y_rot(numpy.deg2rad(rot),c)
                
                a = c1.tolist()
                b = c2.tolist()
                c = c3.tolist()
                A_postion_list = [a[0][0]+a[0][2], a[1][1], a[2][0]+a[2][2]] 
                B_postion_list = [b[0][0]+b[0][2], b[1][1], b[2][0]+b[2][2]]
                C_postion_list = [c[0][0]+c[0][2], c[1][1], c[2][0]+c[2][2]]          
                t.points = [points.points(A_postion_list),points.points(B_postion_list),points.points(C_postion_list)]
                print(A_postion_list,B_postion_list,C_postion_list)
    def everything(self,txyz,rotxyz,sxyz):
        self.scale()
        self.rotate_z(rotxyz[0])
        self.rotate_y(rotxyz[1])
        self.translate(txyz[0],txyz[1],txyz[2])

            
