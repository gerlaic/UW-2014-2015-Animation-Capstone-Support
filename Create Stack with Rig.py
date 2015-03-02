from pymel.core import *
import scene_manager.metaUtil as mu
import random as r

# Constants
NUMBER_OF_STACKS = 12

STACK_ANIM = 'stackAnim'
BUILD_STACK_ATTR = 'buildStack'
STACK_GEO = 'base_stack_geo'

BEND_GRP = 'stack'

STACK_INCREMENT_TY = 6.5


# Add stack building attribute to the anim
anim = PyNode(STACK_ANIM)

anim.addAttr(   BUILD_STACK_ATTR,
                at='long', # Attribute type
                keyable=1,
                min=0,
                max=NUMBER_OF_STACKS,
                defaultValue=NUMBER_OF_STACKS   )
                
stackBuildAttr = anim.attr(BUILD_STACK_ATTR)

# Build stack
for i in xrange(NUMBER_OF_STACKS):
    
    inst = duplicate(STACK_GEO)[0] # Duplicate geo.  Instancing would be preferable,
                                   # but it doesn't work with the bend deformer.
    
    inst.ty.set(i*STACK_INCREMENT_TY) # Move up
    
    inst.ry.set(360*r.random()) # Give random rotation
    
    # Make set driven key using metaUtil shorthand
    mu.sdk( stackBuildAttr, # Driver
            [i, i+1], # Driver values
            inst.visibility, # Driven attribute
            [0, 1]   ) # Driven values corresponding to driver values

stackBuildAttr.set(NUMBER_OF_STACKS)
hide(STACK_GEO) # Hide the base geometry

# Add a bend deformer
select(BEND_GRP)
bend = nonLinear(type='bend')
bendNode = bend[0]
bendTransform = bend[1]

bendNode.lowBound.set(0)
bendNode.highBound.set(2)
bendTransform.ty.set(0)

parent(bendTransform, STACK_ANIM)
hide(bendTransform)


# Shorthands for creating new attribute on an anim then plugging them into other attributes
mu.addAttrToAnim(anim, 'bendAmount', driven=bendNode.curvature, defaultValue=0, minValue=-360, maxValue=360)

mu.addAttrToAnim(anim, 'bendTwist', driven=bendTransform.ry, defaultValue=0, minValue=-360, maxValue=360)

mu.addAttrToAnim(anim, 'bendCutoff', driven=bendTransform.ty, defaultValue=0, minValue=0, maxValue=STACK_INCREMENT_TY*NUMBER_OF_STACKS)
