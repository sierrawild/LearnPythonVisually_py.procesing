size(800,800)
grid = loadImage('grid.png')
image(grid, 0,0)
noFill()
strokeWeight(3)

stroke('#0099ff')

# line(100,100, 400,400)

curve(0,0, 100,100, 400,400, 500,500)

curveTightness(3)

stroke('#ffff00') # yellow
curve(0,250, 100,100, 400,400, 500,250)

stroke('#ff9900') # orange
# control point 1
curve(0,250, 0,250, 100,100, 400,400)
#control point 2 
curve(100,100, 400,400, 500,250, 500,250)


stroke ('#ff99ff') # pink        
cp1x, cp1y = 200, 250
cp2x, cp2y = 320, 420

bezier(400,100, cp1x,cp1y, cp2x,cp2y, 100,400)
# handle
stroke('#ff0000') # red
line(400,100, cp1x,cp1y)
line(100,400, cp2x,cp2y)
