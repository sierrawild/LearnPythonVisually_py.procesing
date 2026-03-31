y_pos = 0

def setup():
    size(1000,1000)
    background('#428af5')
    stroke('#ffffff')
    strokeWeight(2)
    
    
def draw():
    background('#428af5')
    y_pos = sin(frameCount * 0.02) * 50
    
    translate(width/2,height/2 + y_pos)
    
    pushMatrix()

    # head
    fill('#f5ec42')
    circle(0,0,500)
    
    # L eye
    pushMatrix()
    fill('#40403f')
    circle(-100,-50, 100)
    popMatrix()
    # R eye
    pushMatrix()
    fill('#40403f')
    circle(100,-50, 100)
    popMatrix()
    
    # smile
    pushMatrix()
    translate(0,0)
    noFill()
    stroke('#40403f')
    strokeWeight(20)
    arc(0,0, 400, 300, 0.5, 3-0.5)
    popMatrix()
    
    
    popMatrix()
    
