import pygame
import numpy

import matrxies
import mesh
import triangle
import points
fov = 90
near = 1
far = 100
meshd = [
    #SOUTH
    triangle.triangle([points.points([0,0,0]),points.points([0,1,0]),points.points([1,1,0])]),
    triangle.triangle([points.points([0,0,0]),points.points([1,1,0]),points.points([1,0,0])]),
    #EAST
    triangle.triangle([points.points([1,0,0]),points.points([1,1,0]),points.points([1,1,1])]),
    triangle.triangle([points.points([1,0,0]),points.points([1,1,1]),points.points([1,0,1])]),
    #NORTH
    triangle.triangle([points.points([1,0,1]),points.points([1,1,1]),points.points([0,1,1])]),
    triangle.triangle([points.points([1,0,1]),points.points([0,1,1]),points.points([0,0,1])]),
    #WEST
    triangle.triangle([points.points([0,0,1]),points.points([0,1,1]),points.points([0,1,0])]),
    triangle.triangle([points.points([0,0,1]),points.points([0,1,0]),points.points([0,0,0])]),
    #TOP
    triangle.triangle([points.points([0,1,0]),points.points([0,1,1]),points.points([1,1,1])]),
    triangle.triangle([points.points([0,1,0]),points.points([1,1,1]),points.points([1,1,0])]),
    #BOTTOM
    triangle.triangle([points.points([1,0,1]),points.points([0,0,1]),points.points([0,0,0])]),
    triangle.triangle([points.points([1,0,1]),points.points([0,0,0]),points.points([1,0,0])]),
]
cube = mesh.mesh(meshd)
cube.translate(2,0,5)
cube.rotate(5)

def main():
    pygame.init()
    screen = (800,400)
    scale = 100
    circle_pos = (screen[0]/2,screen[1]/2)
    window= pygame.display.set_mode(screen)
    color = (208, 244, 234)
    pygame.display.set_caption("PENUTBUTERJELLYTHELOOOOOOOOOOOOOOONNNNNGGGGGGG WAY")
    run = True
    i = 5
    while run == True:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                run = False
        window.fill(color)
        cube.rotate(i)
        for triangles in meshd:
            p1=triangles.points
            for x in range(0,2):
                a = numpy.matrix(p1[0].return_points())
                b = numpy.matrix(p1[1].return_points())
                c = numpy.matrix(p1[2].return_points())
                a= numpy.c_[a,[1]]
                b= numpy.c_[b,[1]]
                c= numpy.c_[c,[1]]
                c1=matrxies.camra_matrix_function(screen[1]/screen[0],numpy.deg2rad(fov),near,far,a)
                c2=matrxies.camra_matrix_function(screen[1]/screen[0],numpy.deg2rad(fov),near,far,b)
                c3=matrxies.camra_matrix_function(screen[1]/screen[0],numpy.deg2rad(fov),near,far,c)
                
                a = c1.tolist()
                b = c2.tolist()
                c = c3.tolist()
                A_postion_list = [a[0][0], a[1][1], a[2][2] + a[2][3], a[3][3]]
                B_postion_list = [b[0][0], b[1][1], b[2][2] + b[2][3], b[3][3]]
                C_postion_list = [c[0][0], c[1][1], c[2][2] + c[2][3], c[3][3]]
                if A_postion_list[2] != 0:
                    if B_postion_list[2] != 0:
                        if C_postion_list[2] != 0:
                            a_xy = (int((A_postion_list[0]/A_postion_list[2])*scale+circle_pos[0]),int((A_postion_list[1]/A_postion_list[2])*scale+circle_pos[1]))
                            b_xy = (int((B_postion_list[0]/B_postion_list[2])*scale+circle_pos[0]),int((B_postion_list[1]/B_postion_list[2])*scale+circle_pos[1]))
                            c_xy = (int((C_postion_list[0]/C_postion_list[2])*scale+circle_pos[0]),int((C_postion_list[1]/C_postion_list[2])*scale+circle_pos[1]))
                            pygame.draw.line(window,(0,0,0),a_xy,b_xy)
                            pygame.draw.line(window,(0,0,0),b_xy,c_xy)
                            pygame.draw.line(window,(0,0,0),c_xy,a_xy)
                
                
        #pygame.draw.aaline(screen,(0,0,0),pos1,pos2)
        pygame.display.flip()
main()

        