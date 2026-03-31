

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
    strokeWeight(10)
    rotate(-HALF_PI) # set hand to 12
    rotate(TAU / 12*h)
    arc(0,0, 150,0, 0,HALF_PI )
    popMatrix()
    
    # minutes
    pushMatrix()
    strokeWeight(7)
    rotate(-HALF_PI) # set hand to 12
    rotate(TAU / 60*m)
    arc(0,0, 250,0, 0,HALF_PI )
    popMatrix()
    
    # seconds
    pushMatrix()
    strokeWeight(4)
    rotate(-HALF_PI) # set hand to 12
    rotate(TAU / 60*s)
    stroke('#fc4503')
    arc(0,0, 150,0, 0,2 )
    popMatrix()
    
