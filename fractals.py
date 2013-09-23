#!/usr/bin/python
import pygame
import sys

pygame.init()
xd = 1080
yd = 1080
screen = pygame.display.set_mode((xd,yd))

def put_pix(x,y,c):
	x += xd/2 
	y += yd/2 
	screen.set_at((x,y), c)

def f(z,c,d):
	if d <= 0:
		return 1;
	z = z*z + c
	if (z.real * z.real + z.imag * z.imag) >= 4:
		return 1
	else:
		return 1 + f(z,c,d-1)

def normalize(z,zd, zoom):	
	return float(zoom)*2.0*float(z)/float(zd)




def printvector3(x,y,z,c):
    camera = (0.,0.,-1.)
    d = (x-camera[0], y-camera[1], z-camera[2])
    b = [0.,0.]
    b[0] = (-2.0 / d[2] ) * d[0] - 0;
    b[1] = (-2.0 / d[2] ) * d[1] - 0;
    b[0] = b[0] * 100
    b[1] = b[1] * 100
    put_pix(int(b[0]), int(b[1]), depth(z,c[0],c[1],c[2]))

def depth (z,r,g,b):
    z = int(z * 250)
    r -= z
    b += z
    print(r)
    print(z)
    if r > 255:
        r = 255
    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    if b > 255:
        b = 255
    return (r,g,b)




def render(cn, zoomfactor):
	for x in range(-xd/2,xd/2):
		for y in range(-yd/2,yd/2):
			temp = complex(normalize(x,xd,zoomfactor), normalize(y,yd,zoomfactor))
			c = f(temp,cn,511) #512-1
			r = 2 * (c % 64)
			g = 2 * ((c >> 3)% 64)
			b = 2 * ((c >> 6)% 64)
			color = (r,g,b)
			put_pix(int(x),int(y),color)
		pygame.display.update()


def drawvec(x,y,z, dx,dy,dz):

    for i in range(0,400,1):
        di = float(i) /400
        printvector3(x + di*(dx-x), y + di*(dy-y), z+ di*(dz-z), (128,128,0))
    


def cube():
    #topface
    drawvec(-.5,.5,-.5,      .5,.5,-.5);
    drawvec(-.5,.5,.5,      .5,.5,.5);
    drawvec(-.5,.5,.5,      -.5,.5,-.5);
    drawvec(.5,.5,.5,      .5,.5,-.5);
    
    #bottomface
    drawvec(-.5,-.5,-.5,      .5,-.5,-.5);
    drawvec(-.5,-.5,.5,      .5,-.5,.5);
    drawvec(-.5,-.5,.5,      -.5,-.5,-.5);
    drawvec(.5,-.5,.5,      .5,-.5,-.5);

    #sidelines
    drawvec(-.5,.5,-.5,      -.5,-.5,-.5);
    drawvec(-.5,.5,.5,      -.5,-.5,.5);
    drawvec(.5,.5,.5,      .5,-.5,.5);
    drawvec(.5,-.5,-.5,    .5,.5,-.5)

#cn1 = float(sys.argv[1])
#cn2 = float(sys.argv[2])
if (len(sys.argv)> 3):
	zoomfactor = sys.argv[3]
else:
	zoomfactor = 2.0
#cn = complex(cn1,cn2)
#render(cn,zoomfactor)
cube()
pygame.display.update()
input()
