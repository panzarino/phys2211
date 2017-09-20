GlowScript 2.6 VPython
from __future__ import division
from visual import *
scene.width=1024
scene.height=760


# CONSTANTS
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
deltat = 60
t = 0


#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
scene.range=11*Earth.radius
# Add a radius for the spacecraft. It should be BIG, so it can be seen.
craft = sphere(pos=vector(-6.72e+07,-5.76e+06,0), color=color.yellow)
vcraft = vector(705,2587,0)
pcraft = mcraft*vcraft

pscale = Earth.radius / mag(pcraft)
pArrow = arrow(color=color.green)

fscale = Earth.radius / ((G * mEarth * mcraft) / mag(craft.pos - Earth.pos) ** 2)
fArrow = arrow(color=color.cyan)

dpscale = 500 * pscale
dpArrow = arrow(color=color.red)

trail = curve(color=craft.color)    # This creates a trail for the spacecraft
scene.autoscale = 0                 # And this prevents zooming in or out


# CALCULATIONS
while t < 725328:
    rate(20000)   # This slows down the animation (runs faster with bigger number)

    # Add statements here for the iterative update of gravitational
    # force, momentum, and position.
    pcraft_i = pcraft + vector(0,0,0)
    
    r = craft.pos - Earth.pos
    rmag = mag(r)
    Fmag = G * mEarth * mcraft / rmag ** 2
    rhat = norm(r)
    Fnet = -Fmag * rhat
    pcraft = pcraft + Fnet * deltat
    vcraft = pcraft / mcraft
    craft.pos = craft.pos + vcraft * deltat
    
    deltap = pcraft - pcraft_i
    
    pArrow.pos = craft.pos
    pArrow.axis = pscale * pcraft
    fArrow.pos = craft.pos
    fArrow.axis = fscale * Fnet
    dpArrow.pos = craft.pos
    dpArrow.axis = dpscale * deltap

    if rmag < Earth.radius:
        break

    trail.append(pos=craft.pos)  
    t = t+deltat

print("Calculations finished after ",t, "seconds")
print("Final velocity :", vcraft)
print("Final position :", craft.pos)

