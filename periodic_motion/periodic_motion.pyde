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
    
    # white line and a blue circle
    """    
    circle(0,0,radius*2)
    stroke('#ffffff')
    pushMatrix()
    rotate(theta)
    line(0,0,radius,0)
    popMatrix()
    """
    
    # white dot
    noStroke()
    fill('#ffffff')
    # x = cos(theta) * radius
    # y = sin(theta) * radius
    
    # circle
    x,y = circlePoint(theta, radius)
    # circle(x,y,15)
    
    # spiral
    x,y = circlePoint(theta, frameCount/2)
    # circle(x,y,15)
    
    # elipse
    x,y = ellipsePoint(theta, 250, 150)
    circle(x,y,15)
    
    # page 195
    
    
