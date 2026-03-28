size(1000,1000)
background('#004477')
noFill()
stroke('#ffffff')
strokeWeight(3)

    
for i in range(10,40, 5):
    circle(width/2 - i*6, height/2, i * 30)
