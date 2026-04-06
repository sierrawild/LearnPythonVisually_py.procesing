size(561, 768)
art = loadImage('Van_Eyck_-_Arnolfini_Portrait.jpg')
image(art,0,0, width,height)
wait = 1000
def speechBubble(x,y, txt='Hello', type='speech'):
    noStroke()
    pushMatrix()
    translate(x,y)
    
    # tail
    if type == 'speech':
        fill('#ffffff')
        beginShape()
        vertex(0,0)
        vertex(15,-40)
        vertex(35,-40)
        endShape()
    elif type == 'thought':
        fill('#ffffff')
        circle(0,0,8)
        circle(10,-20,20)
        
    
    # bubble
    textSize(15)
    by = -85
    bw = textWidth(txt)
    pad = 20
    rect(0,by, bw+pad*2, 45,10)
    fill('#000000')
    textAlign(LEFT, CENTER)
    text(txt, pad, by+pad)
    
    popMatrix()
    
speechBubble(190,150,'Check out my hat!')
# delay(wait)
speechBubble(316,650, 'Woof')
speechBubble(445,125, 'Meh', 'thought')
