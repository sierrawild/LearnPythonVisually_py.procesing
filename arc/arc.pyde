size(600,600)
background('#004477')
stroke('#FFFFFF')
strokeWeight(3)
noFill()
size = 100


"""
arc( width/2, height/2, size, size,   0,2)
arc( width/2, height/2, size * 1.5, size * 1.5,   0,PI)
arc( width/2, height/2, size * 2, size * 2,   0, PI * 2)
arc( width/2, height/2, size * 1.7, size * 1.7,   3.4,(PI*2)-(PI/2),PIE)
"""

# layer 3
fill('#36FF55')
arc(width/2, height/2, size*4, size*4, -1.3,-0.8, PIE)

# layer 2
fill('#FF98E7')
arc(width/2, height/2, size*3, size*3, -PI,0, PIE)
arc(width/2, height/2, size*3, size*3, -2.4,0, PIE)

fill('#408BFF')
arc(width/2, height/2, size*3, size*3, -1.3,0, PIE)
arc(width/2, height/2, size*3, size*3, -0.3,0, PIE)


# layer 1
fill('#FF36D1')
arc(width/2, height/2, size*2, size*2, -PI,PI, PIE)

fill('#AA36FF')
arc(width/2, height/2, size*2, size*2, -1,0, PIE)

fill('#FF3636')
arc(width/2, height/2, size*2, size*2, 0,PI, PIE)

# circle
fill('#004477')
arc(width/2, height/2, size, size, 0,2*PI)
