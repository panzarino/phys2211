from __future__ import division
from visual import *
from visual.graph import *
scene.y=400

# Turn off autoscaling
autoscale=0

# Create objects: ground, cliff, cannon
# Ground is at y=0
# Ball initial position is initialPos
# Ball initial velocity is initialVel
# Ball size is enlarged for viewing.  For calculations, consider it to be 2 m diameter

# Initial Conditions
initialPos = vector(-500,100,0)
initialVel = vector(60,30,0)

# Setup the scene
ground = box(pos=(0,0,0), length = 1200, height = 1, width = 10, color=color.green)
cliff = box(pos=(initialPos.x-40,initialPos.y/2,0), length = ground.length/2+initialPos.x, height = initialPos.y, width = 10, color=color.green)

# Make Cannon
L=10
wheel = cylinder(pos=initialPos, axis=vector(0,0,1),radius=5, color=color.blue)
cannon = cylinder(pos=initialPos, axis=L*initialVel/mag(initialVel), radius=1)

# Setup ball and trail
ball = sphere(pos=initialPos, radius = 2, color=color.red)
trail = curve(color=ball.color)

# Constants
ball.m = 10		# ball's mass (10 kg)
g = 9.8			# gravitational acceleration
pScale = 0.05	        # scale for momentum arrow
fScale = 0.1	        # scale for force arrow

# Drag constants
airDensity = 1.293		# density of air near the surface of the Earth
areaBall = pi*1**2		# cross-sectional area of the ball (diameter 2m)
dragCoeff = 0.1			# drag coefficient for this ball

# Initialize ball's momentum
ball.p=ball.m*initialVel

# Time Setup
t=0
deltat=1e-3

#Setup Force and momentum Arrows
pArrow = arrow(pos=initialPos, color=color.red)
fArrow = arrow(pos=initialPos, color=color.white)
fperpArrow = arrow(pos=initialPos, color=color.blue)
fparaArrow = arrow(pos=initialPos, color=color.green)

Kgraph=gcurve(color=color.red)
Ugraph=gcurve(color=color.cyan)
KplusUgraph=gcurve(color=color.yellow)

# The while loop below models the motion of the ball after it leaves the cannon
# Motion coninues until the ball's height reaches zero.

# MODIFY THE CODE IN THIS LOOP according to the instructions in the lab instructions.

while ball.pos.y>0:
    
    rate(500)
    # Calculate the net force on the ball
    F_grav = vector(0, -g * ball.m,  0)
    F_air = -.5 * dragCoeff * airDensity * areaBall * (mag(initialVel) ** 2) * norm(initialVel)
    F_net = F_grav + F_air

        
    # Update the momentum of the ball
    ball.p += F_net * deltat


        
    # Update the position of the ball
    initialVel = ball.p / ball.m
    ball.pos += initialVel * deltat
    
    
    
    # Update the trails of the ball
    trail.append(pos=ball.pos)
        
        
        
    # Calculate the force components
    F_parallel = dot(F_net, norm(ball.p)) * norm(ball.p)
    F_perpendicular = F_net - F_parallel
        
        
        
    # Update the arrows representing the momentum, force and force components
    pArrow.pos = ball.pos
    pArrow.axis = ball.p * pScale
    fArrow.pos = ball.pos
    fArrow.axis = F_net * fScale * 3
    fperpArrow.pos = ball.pos
    fperpArrow.axis = F_perpendicular * fScale * 3
    fparaArrow.pos = ball.pos
    fparaArrow.axis = F_parallel * fScale * 3

    #graphs
    K = .5 * ball.m * mag(initialVel) ** 2
    U = g * ball.m * ball.pos.y
    
    Kgraph.plot(pos=(t,K))
    Ugraph.plot(pos=(t,U))
    KplusUgraph.plot(pos=(t,K+U))


    # Update time
    t += deltat
        		

print("Package hit the ground")
print("time=", t, "s")
print("mag(velocity)=", mag(initialVel))
print("velocity x=", initialVel.x)
print("velocity y=", initialVel.y)
print("pos x=", ball.pos.x)

# In addition to time, print the final values of the following quantities:
# magnitude of ball's velocity
# x-component of ball's velocity
# y-component of ball's velocity
# x-position of ball
      
