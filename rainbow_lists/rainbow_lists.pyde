size(500, 500)
noStroke()
background('#004477')
bands = [
'#FF0000',  # red
'#FF9900',  # orange
'#FFFF00',  # yellow
'#00FF00',  # green
'#0099FF',  # blue
'#6633ff',  # violet
]

# red band
translate(0,100)
# fill(bands[0])
# rect(0,0,width, 50)

for band in bands:
    fill(band)
    rect(0,0,width,50)
    translate(0,50)
