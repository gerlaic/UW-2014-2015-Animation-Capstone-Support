#Random Rotate
from pymel.core import *
import random

#edge loop
#mel.eval('polySplitRing -ch on -splitType 2 -divisions 4 -useEqualMultiplier 1 -smoothingAngle 30 -fixQuads 1')

#mel.eval('polySplitRing -ch on -splitType 2 -divisions 4 -useEqualMultiplier 1 -smoothingAngle 30 -fixQuads 1')

sel = ls(selection = True)
deg = -5 + random.random()*10
rotate(sel,0,deg,0)
