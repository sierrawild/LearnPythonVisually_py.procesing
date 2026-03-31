size(800,800)
noFill()
noStroke()
grid = loadImage('grid.png')
image(grid,0,0)
grido = loadImage('grid-overlay.png')
###########

translate(400,400)
rotate(QUARTER_PI)
scale(0.5)

pushMatrix()
shearX(PI/4)
translate(-400,-400)
image(grido, 0 , 0)
fill('#ff0000') # red
square(0,0,100)
popMatrix()

pushMatrix()
translate(100,0)
image(grido, 0 , 0)
fill('#ffff00') # yellow
square(0,0,100)
popMatrix()
