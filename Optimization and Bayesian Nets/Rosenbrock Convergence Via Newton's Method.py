from sympy import *
import numpy as np
from scipy import linalg

x,y = symbols('x y', real=True)

def d1(func):
    
    dx = diff(func,x)
    dy = diff(func,y)
    return [dx,dy]

def d2(func):
    
    dx = diff(func,x)
    dy = diff(func,y)
    
    dxx = diff(dx,x)
    dxy = diff(dx,y)
    dyx = diff(dy,x)
    dyy = diff(dy,y)
    
    return [[dxx,dxy],[dyx,dyy]]
  
  
  def converge(s1,s2):    
    
    f = 100*(y-(x**2))**2 + (1-x)**2
    x0 = s1
    y0 = s2

    j = d1(f)
    h = d2(f)
    j1 = j[0].subs([(x, x0), (y, y0)])
    j2 = j[1].subs([(x, x0), (y, y0)])
    res1 = Matrix([j1,j2])
    h1 = h[0][0].subs([(x, x0), (y, y0)])
    h2 = h[0][1].subs([(x, x0), (y, y0)])
    h3 = h[1][0].subs([(x, x0), (y, y0)])
    h4 = h[1][1].subs([(x, x0), (y, y0)])
    res2 = Matrix([[h1,h2],[h3,h4]])
    res2neg = Matrix([[-h1,-h2],[-h3,-h4]])
    res2neg = res2neg.inv()

    d0 = res2neg.dot(res1)
    k = 0
    e = 10**(-4)

    while (res1.T).dot(res1) > e:

        a = 1
        c = 0.2
        p = 0.1

        d00 = d0[0]*a
        d01 = d0[1]*a
        m2 = Matrix([d00,d01])
        inner = Matrix([x0,y0])+m2
        func1 = f.subs([(x, inner[0]), (y, inner[1])])
        func2 = f.subs([(x, x0), (y, y0)])
        j1 = j[0].subs([(x, x0), (y, y0)])
        j2 = j[1].subs([(x, x0), (y, y0)])
        newj = Matrix([j1,j2]).T
        final = newj.dot(d0)
        while func1 > (func2 + c*a*final):

            a = p*a
            
        d00 = d0[0]*a
        d01 = d0[1]*a
        m2 = Matrix([d00,d01])
        inner = Matrix([x0,y0])+m2
        x0 = inner[0]
        y0 = inner[1]
        print("X, Y: ",x0,y0)
        print("Alpha: ",a)
        
        
        j1 = j[0].subs([(x, x0), (y, y0)])
        j2 = j[1].subs([(x, x0), (y, y0)])
        res1 = Matrix([j1,j2])
        h1 = h[0][0].subs([(x, x0), (y, y0)])
        h2 = h[0][1].subs([(x, x0), (y, y0)])
        h3 = h[1][0].subs([(x, x0), (y, y0)])
        h4 = h[1][1].subs([(x, x0), (y, y0)])
        res2 = Matrix([[h1,h2],[h3,h4]])
        res2neg = Matrix([[-h1,-h2],[-h3,-h4]])
        res2neg = res2neg.inv()

        d0 = res2neg.dot(res1)

        k += 1
        print((res1.T).dot(res1))
        
      
converge(1.2,1.2)
converge(-1.2,1)
