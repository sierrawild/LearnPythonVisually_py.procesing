import json
jsondata = open('coffees.json')
coffees = json.load(jsondata)

size(800,800)
background('#004477')
mug = 120
spacing = 230
col = 1

translate(100,100)

for coffee in coffees:
    
    y_offset = mug
    for i in coffee['ingredients']:
        fill(i['color'])
        pushMatrix()
        translate(0,y_offset)
        rect(0, - i['quantity'], mug, i['quantity'])
        y_offset -= i['quantity']
        popMatrix()
    
    # mug
    strokeWeight(5)
    stroke('#ffffff')
    noFill()
    square(0,0, mug)
    arc(mug, mug/2, 40, 40, -HALF_PI, HALF_PI)
    arc(mug, mug/2, 65, 65, -HALF_PI, HALF_PI)
    
    # label
    fill('#ffffff')
    textSize(16)
    label = coffee['name']
    text(label, mug/2-textWidth(label)/2, mug+40)
    
    if col == 3:
        translate(spacing*-2, spacing)
        col = 1
    else:
        translate(spacing, 0)
        col += 1
             
