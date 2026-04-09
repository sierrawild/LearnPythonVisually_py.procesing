def setup():
    size(800, 600)
    
radius = 200
theta = 1
period = 2.1

def circlePoint(t,r):
    x = cos(t) * r
    y = sin(t) * r
    return[x,y]

def ellipsePoint(t, hr, vr):
    x = cos(t) * hr
    y = sin(t) * vr
    return x,y

def draw():
    global theta
    theta -= TAU / (frameRate * period)
        
    background('#004477')
    noFill()
    strokeWeight(3)
    stroke('#0099FF')
    line(width/2, height, width/2, 0)
    line(0, height/2, width, height/2)
    # flip the y-axis
    scale(1, -1)
    translate(0, -height)
    # reposition the origin
    translate(width/2, height/2)
    
    amplitude = radius
    stroke('#ffffff')
    strokeWeight(7)
    strokeJoin(ROUND)
    noFill()
    beginShape()
    for i in range(51):
        f = 0.125*2
        t = theta + i * f
        x = -400 + i * 16
        y = sin(t)* amplitude  
        vertex(x,y)
    endShape()
    
