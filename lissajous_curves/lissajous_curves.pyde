def lissajousPoint(t,A,B,a,b):
    x = cos(t * a) * A
    y = sin(t * b) * B
    return [x,y]

def setup():
    size(800,600)
    frameRate(90)
    background('#004477')
    fill('#ffffff')
    noStroke()
    
theta = 0
period = 4

def draw():
    global theta
    theta += TAU / (frameRate * period)
    
    # flip y axis and center the origin
    scale(1,-1)
    translate(width/2,height/2-height)
    
    x,y = lissajousPoint(theta, 200, 100, 3, 5)
    circle(x,y, 15)
