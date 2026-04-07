def setup():
    size(1000,1000)
    
def draw():
    background('#0C72BF')
    stroke('#6DABD8')
    strokeWeight(5)
        
    line(width/2,0,width/2,height)
    line(0,height/2, width,height/2)
    
    translate(500,500)
    scale(1,-1)
    
    noFill()
    circle(0,0, 500)
    ###############
    
    
    
    
