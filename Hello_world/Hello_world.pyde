size(500,500)
background("#004488")
print("Hello, world!")

# stroke
stroke("#ffffff")
strokeWeight(5)

# blue sqrs
strokeJoin(MITER)
fill("#1769BF")
rect(100,100,200,350)
rect(10,15, 20, 40)

# orange sqr
strokeJoin(BEVEL)
fill("#FF9900")
rect(50,250, 150, 150)

# # no fill
strokeJoin(ROUND)
noFill()
square(250, 80, 150)
