GlowScript 2.6 VPython
from __future__ import division                 ## treat integers as real numbers in division
from visual import *
from visual.graph import *
scene.width=600
scene.height = 760



## constants and data
g = 9.8
mball = 0.1404   ## change this to the Mass you used in the lab for the oscillation experiments
L0 = 0.3    ## use the relaxed length from your previous lab
ks = 12      ## change this to the spring constant you measured (in N/m)
deltat = 1e-3  ## change this to be about 1/1000 of your measured period when you used Mass 2

t = 0       ## start counting time at zero

## objects
ceiling = box(pos=vector(0,0,0), size = vector(0.2, 0.01, 0.2))         ## origin is at ceiling
ball = sphere(pos=vector(-0.1095,-0.1098,-0.1596), radius=0.025, color=color.orange) ## note: spring initially compressed
spring = helix(pos=ceiling.pos, color=color.cyan, thickness=.003, coils=40, radius=0.015) ## change the color to be your spring color
parrow = arrow(color=color.magenta, pos=ball.pos, axis=vector(0,0,0))
farrow = arrow(color=color.red, pos=ball.pos, axis=vector(0,0,0))
trail = curve(color=ball.color)

spring.axis = ball.pos - ceiling.pos

## Setup graphing windows
gdisplay(width=500, height=250, x=600, y=1)
gdisplay(width=500, height=250, x=600, y=300)

ygraph = gcurve(color=color.yellow)
pgraph = gcurve(color=color.cyan)

## initial values
ball.p = mball*vector(0.484,0.153,0.146)

## improve the display
scene.autoscale = 0             ## don't let camera zoom in and out as ball moves
scene.center = vector(0,-L0,0)   ## move camera down to improve display visibility

## calculation loop

while t < 9.74:           ## make this short to read period off graph
    rate(1000)

## calculate force on ball by spring (note: requires calculation of L_vector)


    force = -ks * (mag(spring.axis) - L0) * norm(spring.axis)

## calculate net force on ball (note: has two contributions)

    # gravity
    force += vector(0, -mball * g, 0)

## apply momentum principle

    ball.p += force * deltat

## update position

    ball.pos += (ball.p/mball) * deltat

## trail
    trail.append(pos=ball.pos)

## update arrows
    parrow.pos = ball.pos
    parrow.axis = norm(ball.p) * .1

    farrow.pos = ball.pos
    farrow.axis = norm(force) * .1

## update axis of spring

    spring.axis = ball.pos - ceiling.pos

## update graph
    ygraph.plot(pos=(t, ball.pos.y))
    pgraph.plot(pos=(t, mag(ball.p)))
## update time
    t = t + deltat
print (ball.pos)
print ((ball.p)/ mball)
