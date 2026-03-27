size(800,800)
grid = loadImage('grid.png')
image(grid,0,0)
noFill()
stroke('#ffffff')
strokeWeight(3)

beginShape()
vertex(100,100)
vertex(200,100)
vertex(200,200)
vertex(100,200)
endShape()

# S shape
beginShape()
vertex(400,200)
bezierVertex(300,300, 500,500, 400,600)
endShape()

# heart
beginShape()
vertex(600, 240)
bezierVertex(650,150, 780,300, 600,400)
bezierVertex(420,300, 550,150, 600,240)
endShape()

# circle
fill('#6633FF')
beginShape()
vertex(200,500)
bezierVertex(255,500, 300,545, 300,600)
bezierVertex(300,655, 255,700, 200,700)
bezierVertex(145,700, 100,655, 100,600)
bezierVertex(100,545, 145,500, 200,500)

beginContour()
vertex(180,580)
vertex(180,620)
vertex(220,620)
vertex(220,580)
vertex(180,580)
endContour()
endShape()
