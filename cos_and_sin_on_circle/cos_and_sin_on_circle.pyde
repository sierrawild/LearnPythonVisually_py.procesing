def setup():
    size(2000,2000)
    
    font = createFont("Arial Black", 34)
    textFont(font)

r = 250
angle = 1
period = 10

sinCol = '#03c0ff'
cosCol = '#ff8903'

def draw():
    global angle
    background('#0C72BF')
    stroke('#6DABD8')
    strokeWeight(5)
        
    line(width/2,0,width/2,height)
    line(0,height/2, width,height/2)
    
    translate(width/2,height/2)
    scale(1,-1)
    
    noFill()
    circle(0,0, r * 2)
    ###############
    
    fill('#ffffff')
    stroke('#ffffff')
    
    angle -= TAU / (frameRate * period)
    
    x = cos(angle) * r
    y = sin(angle) * r
    
      
    # blue sin
    stroke(sinCol)
    for i in range(int(abs(sin(angle)*20))):
            if sin(angle) < 0:
                i *= -1
            circle(x,13*i, 5)
    # line(x,0,x,y)
    
    # orange cos
    stroke(cosCol)
    for i in range(int(abs(cos(angle)*20))):
        if cos(angle) < 0:
            i *= -1
        circle(13*i,0, 5)
    # line(0,0, x,0)
    
    
    # point and white line 
    stroke('#ffffff') 
    circle(x,y, 10)
    line(0,0, x,y)
    
    # text bottom left
    pushMatrix()
    pushStyle()
    translate(-400,-400)
    scale(1,-1)
    
    # textSize(25)
    fill(sinCol)
    text('SIN = {:.3f}'.format(sin(angle)),0,0)
    fill(cosCol)
    text('COS = {:.3f}'.format(cos(angle)),0,40)
    
    popStyle()
    popMatrix()
    
    
