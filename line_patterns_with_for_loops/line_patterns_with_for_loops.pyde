size(1000,1000)
background('#004477')
noFill()
stroke('#ffffff')
strokeWeight(3)

x1, y1 = 60,80
x2, y2 = 300,30

for i in range(0,40,2):
    line(x1,y1 + i*10, x2,y2+ 10*i)
    

x1, y1 = 400,30
x2, y2 = 400+(300-60), 80

for i in range(0,21,2):
    line(x1,y1 + i*i, x2,y2 + i* i)
    
# overlaping lines
x1, y1 = width/2 - 240, height/2 + 50
x2, y2 = width/2, height/2

for i in range(0,30, 4):
    line(x1,y1 + i * 10, x2, y2 + i * 10)

x3, y3 = x1, y1
x1, y1 = x2, y2
x2, y2 = x3 + 240*2, y3

for i in range(2,34, 4):
    line(x1,y1 + i * 10, x2, y2 + i * 10)
