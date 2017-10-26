from __future__ import division
from visual.graph import *
from visual import *

scene.width=1024
scene.height=760
scene.y = 400

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
craft = sphere(pos=vector(10*Earth.radius, 0 ,0), color=color.yellow)
vcraft = vector(0,3.286e3,0)
pcraft = mcraft*vcraft
#pArrow = arrow(color=color.green)
#fArrow = arrow(color=color.cyan)
Fnet_tangent = arrow(color=color.yellow)
Fnet_perp = arrow(color=color.magenta)
dpArrow = arrow(color=color.red)
pcraft_i = vector(0,0,0)
momentum_Moon = vector(0,0,0)
deltap = vector(0,0,0)

Moon.v = vector(0,math.sqrt((G*mEarth/(mag(Moon.pos-Earth.pos)))),0)
momentum_Moon = Moon.v * mMoon

# MORE CONSTANTS
pScale = Earth.radius/mag(pcraft)
dpscale = 500*pScale
fscale = Earth.radius/(G*((mcraft*mEarth)/((mag(craft.pos-Earth.pos))**2)))


trail = curve(color=craft.color)    # This creates a trail for the spacecraft
mTrail = curve(color=Moon.color)
#scene.autoscale = 1                 # And this prevents zooming in or out
scene.range = (5e8,5e8,5e8)

Fnet = vector(0,0,0)

U_graph = gcurve(color=color.blue) #A plot of the Potential energy
K_graph = gcurve(color=color.yellow) #A plot of the Kinetic energy
Energy_graph = gcurve(color=color.green) #A plot of the Total energy

# CALCULATIONS
while t < 10*365*24*60*60:
    rate(10000)   # This slows down the animation (runs faster with bigger number)
    #scene.center = craft.pos
    scene.center = Earth.pos

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


    r_EarthMoon = Moon.pos - Earth.pos#Relative position vector from Earth to Moon
    r_craftMoon = Moon.pos - craft.pos#Relative position vector from spacecraft to Moon
    Force_EarthMoon = norm(r_EarthMoon) * -G * ((mEarth * mMoon) / mag(r_EarthMoon)**2)#Force on Moon due to Earthdddddddd
    Force_craftMoon = norm(r_craftMoon) * -G * ((mcraft * mMoon) / mag(r_craftMoon)**2)#Force on Moon due to spacecraft
    Fnet_Moon = Force_EarthMoon + Force_craftMoon #Net force on Moon


    # Uncomment these two lines to exit the loop if
    # the spacecraft crashes onto the Earth.
    if rmag < Earth.radius or mag(mR) < Moon.radius: 
        break

    pcraft_i = vector(0,0,0) + pcraft
    pcraft = pcraft + Fnet * deltat
    momentum_Moon = momentum_Moon + Fnet_Moon * deltat
    deltap = pcraft - pcraft_i
    vcraft = pcraft/mcraft
    craft.pos = craft.pos + (vcraft * deltat)
    Moon.pos = Moon.pos + (momentum_Moon/mMoon) * deltat
    #print craft.pos

    K_craft = .5 * mcraft * mag(vcraft) ** 2
    U_craft_Earth = -G * (mcraft * mEarth) / mag(r)
    #U_craft_Moon = -G * (mcraft * mMoon) / mag(mR)
    #E = K_craft + U_craft_Earth + U_craft_Moon


    #pArrow.pos = craft.pos
    #pArrow.axis = pcraft * pScale

    
    Fnet_tangent.pos = craft.pos
    Fnet_tangent.axis = ((mag(pcraft) - mag(pcraft_i)) / deltat) * norm(pcraft) * 100000

    Fnet_perp.pos = craft.pos
    Fnet_perp.axis = (Fnet - Fnet_tangent.axis/100000) *100000

    dpArrow.pos = craft.pos
    dpArrow.axis = deltap*dpscale

    trail.append(pos=craft.pos)  
    mTrail.append(pos=Moon.pos)
    #U_graph.plot(pos=(rmag,U_craft_Earth+U_craft_Moon)) #Potential energy as a function of time
    K_graph.plot(pos=(rmag,K_craft)) #Kinetic energy as a function of time
    #Energy_graph.plot(pos=(rmag,E)) #Total energy as a function of time
    t = t+deltat
print "final velocity: "
print vcraft
print "final position: "
print craft.pos
print "grav force: "
print Fnet
print mag(Fnet_tangent.axis)/100000
print mag(Fnet_perp.axis)/100000
print("Calculations finished after ",t, "seconds")
