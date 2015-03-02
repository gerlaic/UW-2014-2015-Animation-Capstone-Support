#random generate stack
from pymel.core import *
import random

sel = ls(selection = True)

for i in range(1,25):
    print(sel)
    new = duplicate(sel[random.randint(1,3)-1])[0]
    x = -0.3+random.random()*0.6
    z = -0.3+random.random()*0.6
    move(new,x,0.56*i,z)
    deg = -3+random.random()*6
    rotate(new,0, deg, 0)
