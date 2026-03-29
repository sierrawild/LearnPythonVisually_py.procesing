speed = 7
y = 100
yspeed = speed
x = 100
xspeed = speed

def setup():
    size(800,600)
    fill('#0099ff')
    textSize(50)
    
def draw():
    global y, yspeed, x, xspeed
    background('#000000')
    y += yspeed
    x += xspeed
    text('DVD', x, y)
    # my solution
    if y > height:
        yspeed *= -1
    if y - 40 < 0 and yspeed < 0:
        yspeed *= -1   
    
    if x + 100 > width:
        xspeed *= -1
    if x < 0 and xspeed < 0:
        xspeed *= -1
        
    # book solution
    """
    if y < 0+50 or y > height:
        yspeed *= -1

    if x < 0 or x > width - textWidth('DVD'):
        xspeed *= -1
    """
