GlowScript 2.6 VPython

scene.range = 20
scene.width = 1024
scene.height = 800
scene.background = vec(0.95,0.95,0.95)
box()


def arrowGenerator(arrowPosition,arrowAxis,arrowColor):
    arrow(pos=arrowPosition,axis=arrowAxis,color=arrowColor)
    
def drawTrajectory(n,list_of_locations,list_of_avgmomenta,pscale):
    scene2 = display(x=0, y=0, width=1024, height=800, range=20, background=vec(0.95,0.95,0.95))
    trail=curve(color=color.blue)

    i=0

    while i<n:

        sphere(pos=list_of_locations[i],radius=0.75,color=color.blue)
#        label(pos=list_of_locations[i], text='%1.0f' % i)

        if i<n-1:
            arrowGenerator(list_of_locations[i],pscale*list_of_avgmomenta[i],color.green)

        trail.append(list_of_locations[i])

        i=i+1


##################################################################
########## !!!!! DO NOT EDIT CODE ABOVE THIS LINE !!!!! ##########
########## Doing so may render your program inoperable. ##########
##################################################################



n=4          ## Number of snapshots
deltat=1     ## Time between snapshots
mass=5       ## Mass of the particle
pscale=1e-1
fscale=1



##################################################################
########## !!!!! DO NOT EDIT CODE BELOW THIS LINE !!!!! ##########
########## Doing so may render your program inoperable. ##########
##################################################################

list_of_locations=[]
ballcount = 0

while ballcount<n:
    m = scene.waitfor('click')
    loc = m.pos
    ball = sphere(pos=loc, radius=0.75, color=color.blue)
    list_of_locations.append(ball.pos)
    ballcount = ballcount + 1
    
print(list_of_locations)

for thislocation in list_of_locations:
    print("Location is:", thislocation)

j=0
list_of_avgmomenta=[]

while j<n-1:

    rate(5)
    displacement=list_of_locations[j+1]-list_of_locations[j]
    avgmomentum = mass*displacement/deltat
    list_of_avgmomenta.append(avgmomentum)
    print("Average Momentum between ", j, " and ",j+1, ":", avgmomentum)
    arrowGenerator(list_of_locations[j],pscale*avgmomentum,color.green)

    j=j+1
    
k=0
list_of_avgforces=[]

while k<n-2:

    rate(5)
    momentumchange=(list_of_avgmomenta[k+1]-list_of_avgmomenta[k])
    avgforce=momentumchange/deltat
    list_of_avgforces.append(avgforce)
    print("Average force bewtween ", k, " and ", k+2,":", avgforce)
    arrowGenerator(list_of_locations[k+1],fscale*avgforce,color.red)
    
    k=k+1


## Uncomment the line below only AFTER you finished writing the code above
print('Click to display trajectory.')

x = True

while x:

    m=scene.waitfor('click')
    drawTrajectory(n,list_of_locations,list_of_avgmomenta,pscale)
    x = False

