size(1000,1000)
background('#004477')
noFill()
stroke('#ffffff')
strokeWeight(3)

i = 0
while i < 40:
    circle(width/2 + i*6, height/2, i * 30)
    i += 1
    
for i in range(40):
    circle(width/2 - i*6, height/2, i * 30)
