size(500,320)
background('#004477')
fill('#ffffff')
stroke('#0099ff')
strokeWeight(3)

pangram = 'Qiartz jock vends BMW glyph fix'
p = pangram
text(p,0,50)

textSize(20)
text(p,0,100)

line(textWidth(p),0,textWidth(p),height)

seriffont = createFont('Times New Roman Bold',20)

textFont(seriffont)
text(p,0,150)

textLeading(10)
text(p,0,200,250,100)

textAlign(RIGHT)
text(p,0,250,250,100)
