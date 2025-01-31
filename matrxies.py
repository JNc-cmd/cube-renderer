import numpy
def camra_matrix_function(displayratio, fov, near_legnth, far_length, xyz_matrix):
    camra_matrix = numpy.matrix([
        [(displayratio)+(1/(numpy.tan(fov/2))),0,0,0],
        [0,(1/(numpy.tan(fov/2))),0,0],
        [0,0,far_length/(far_length-near_legnth),(-far_length*near_legnth)/(far_length-(near_legnth))],
        [0,0,1,0]
    ])
    return numpy.multiply(camra_matrix,xyz_matrix)
def translation(dx,dy,dz,matrix):
    translation_matrix = numpy.matrix([
        [1,0,0,dx],
        [0,1,0,dy],
        [0,0,1,dz],
        [0,0,0,1]
    ])
    return numpy.multiply(translation_matrix,matrix)
def scale(dx,dy,dz,matrix):
    scale_matrix = numpy.matrix(
        [dx,0,0,0],
        [0,dy,0,0],
        [0,0,dz,0],
        [0,0,0,1],
    )
    return numpy.multiply(scale_matrix,matrix)
def zrot(rot,matrix):
    zrot_matrix = numpy.matrix([
      [numpy.cos(rot),-numpy.sin(rot),0,0],
      [numpy.sin(rot),numpy.cos(rot),0,0],
      [0,0,1,0],
      [0,0,0,1]  
    ])
    return numpy.multiply(zrot_matrix,matrix)
def y_rot(rot,matrix):
    yrot_matrix = numpy.matrix([
        [numpy.cos(rot),0,numpy.sin(rot),0],
        [0             ,1,             0,0],
        [-(numpy.sin(rot)),0,numpy.cos(rot),0],
        [0             ,0,             0,1]
    ])
    return numpy.multiply(yrot_matrix,matrix)
def x_rot(rot,matrix):
    xrot_matrix = numpy.matrix([
        [1,0,0,0],
        [0,numpy.cos(rot),-numpy.sin(rot),0],
        [0,numpy.sin(rot),numpy.cos(rot),0],
        [0,0,0,1]
    ])
    return numpy.multiply(xrot_matrix,matrix)