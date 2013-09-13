import pygame

pygame.init()
xd = 1440
yd = 1440
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

def normalize(z,zd):	
	return 4.0*z/zd



def render(cn):
	for x in range(-xd/2,xd/2):
		for y in range(-yd/2,yd/2):
			temp = complex(normalize(x,xd), normalize(y,yd))
			c = f(temp,cn,511) #512-1
			r = 2 * (c % 64)
			g = 2 * ((c >> 3)% 64)
			b = 2 * ((c >> 6)% 64)
			color = (r,g,b)
			put_pix(x,y,color)
		pygame.display.update()


cn1 = float(input("enter a number"))
cn2 = float(input("enter another number"))
cn = complex(cn1,cn2)
render(cn)
pygame.display.update()
input()
