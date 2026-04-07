def setup():
    size(1000,1000)

r = 250
angle = 1
period = 10

def draw():
    global angle
    background('#0C72BF')
    stroke('#6DABD8')
    strokeWeight(5)
        
    line(width/2,0,width/2,height)
    line(0,height/2, width,height/2)
    
    translate(500,500)
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
    stroke('#03c0ff')
    line(x,0,x,y)
    
    # orange cos
    stroke('#ff8903')
    line(0,y, x,y)
    
    # point and white line 
    stroke('#ffffff') 
    circle(x,y, 10)
    line(0,0, x,y)
    
    
