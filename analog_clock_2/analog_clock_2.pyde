

d = day()
mm = month()
y = year()
date = str(d) + "/" + str(mm) + "/" + str(y)

def setup():
    size(600, 600)
    frameRate(1)
    noFill()
    stroke('#FFFFFF')
def draw():
    h = hour()
    m = minute()
    s = second()
    
    background('#004477')
    stroke('#FFFFFF')
    strokeCap(SQUARE)
    
    # date
    pushMatrix()
    textSize(32)
    translate(400,550)
    text(date, 0,0)
    popMatrix()
    # time printed
    pushMatrix()
    textSize(32)
    translate(400,500)
    text("{}:{}:{}".format(h,m,s), 0,0)
    # print("{}:{}:{}".format(h,m,s))
    popMatrix()
    
    # analog clock
    translate(width/2,height/2)
    strokeWeight(3)
    circle(0,0,350)
    
    # hour
    pushMatrix()
    strokeWeight(30)
    rotate(-HALF_PI) # set hand to 12
    rotate(TAU / 12*h)
    arc(0,0, 250,250, -0.2,0.2 )
    popMatrix()
    
    # minutes
    pushMatrix()
    strokeWeight(20)
    rotate(-HALF_PI) # set hand to 12
    # rotate(TAU / 60*m)
    arc(0,0, 300,300, -0.2,0.2 )
    popMatrix()
    
    # seconds
    pushMatrix()
    strokeWeight(8)
    rotate(-HALF_PI) # set hand to 12
    rotate(TAU / 60*s)
    stroke('#fc4503')
    arc(0,0, 350,350, 0,0.3 )
    popMatrix()
    
