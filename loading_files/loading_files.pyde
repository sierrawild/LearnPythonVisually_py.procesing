size(800,800)
background('#004477')
tsv = loadStrings('list_of_best-selling_video_games.tsv')
noStroke()

translate(50, 50)
r = 255
for entry in tsv[1:]:
    entry1 = entry.split('\t')
    rank = entry1[0]
    title = entry1[1]
    sales1 = int(entry1[2])
    txt = '{}.{} - {}'.format(rank,title, sales1)
    
    fill(r, 100, 100)
    rect(0,0, sales1/ 300000, 50)
    translate(0,50)
    r *= 0.92
    
     # print names
    pushMatrix()
    translate(20,-20)
    textSize(20)
    fill('#000000')
    text(txt, 0,0)
    popMatrix()
