from __future__ import division
from visual import *
scene.width=1024
scene.height=760

# CONSTANTS
G = 6.7e-11
mEarth = 6e24
mMoon = 7e22
mcraft = 15e3
deltat = 10
t = 0


#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=vector(0,0,0), radius=6.4e6, color=color.cyan)
Moon = sphere(pos=(Earth.pos + vector(4e8,0,0)), radius=1.75e6, color=color.white)
scene.range=25*Earth.radius
# Add a radius for the spacecraft. It should be BIG, so it can be seen.
craft = sphere(pos=vector(-10*Earth.radius, 0 ,0), color=color.yellow)
vcraft = vector(0,3.27e3,0)
pcraft = mcraft*vcraft
#pArrow = arrow(color=color.green)
#fArrow = arrow(color=color.cyan)
Fnet_tangent = arrow(color=color.yellow)
Fnet_perp = arrow(color=color.magenta)
dpArrow = arrow(color=color.red)
pcraft_i = vector(0,0,0)
deltap = vector(0,0,0)


# MORE CONSTANTS
pScale = Earth.radius/mag(pcraft)
dpscale = 500*pScale
fscale = Earth.radius/(G*((mcraft*mEarth)/((mag(craft.pos-Earth.pos))**2)))


trail = curve(color=craft.color)    # This creates a trail for the spacecraft
scene.autoscale = 0                 # And this prevents zooming in or out
#scene.range = (7e8,7e8,7e8)

Fnet = vector(0,0,0)

# CALCULATIONS
while t < 67740:#3600 * 24 * 60:#10*365*24*60*60:
    rate(5000)   # This slows down the animation (runs faster with bigger number)
    scene.center = craft.pos

    # Add statements here for the iterative update of gravitational
    # force, momentum, and position. 
    mR = craft.pos - Moon.pos
    r = craft.pos - Earth.pos
    rmag = sqrt((r.x)**2 + (r.y)**2  +(r.z)**2)

    Fmag = G*((mcraft*mEarth)/((rmag)**2))
    FmagMoon = G*((mcraft*mMoon)/(mag(mR)**2))
    
    
    rhat = r/rmag

    Fnet = rhat * -Fmag
    Fnet += norm(mR) * -FmagMoon
    #print ("Fnet =", Fnet)

    # Uncomment these two lines to exit the loop if
    # the spacecraft crashes onto the Earth.
    if rmag < Earth.radius or mag(mR) < Moon.radius: 
        break

    pcraft_i = vector(0,0,0) + pcraft
    pcraft = pcraft + Fnet * deltat
    deltap = pcraft - pcraft_i
    vcraft = pcraft/mcraft
    craft.pos = craft.pos + (vcraft * deltat)
    #print craft.pos


    #pArrow.pos = craft.pos
    #pArrow.axis = pcraft * pScale

    
    Fnet_tangent.pos = craft.pos
    Fnet_tangent.axis = ((mag(pcraft) - mag(pcraft_i)) / deltat) * norm(pcraft) * 100000

    Fnet_perp.pos = craft.pos
    Fnet_perp.axis = (Fnet - Fnet_tangent.axis/100000) *100000

    dpArrow.pos = craft.pos
    dpArrow.axis = deltap*dpscale

    trail.append(pos=craft.pos)  
    t = t+deltat
print "final velocity: "
print vcraft
print "final position: "
print craft.pos
print "grav force: "
print Fnet
print("Calculations finished after ",t, "seconds")
