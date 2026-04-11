class Amoeba(object):
    
    def __init__(self, x, y, diameter, xspeed, yspeed):
        print('amoeba initialized')
        self.location = PVector(x,y)
        self.location.x= x
        self.location.y= y
        self.d = diameter
        self.nucleus = {
            'fill': ['#ff0000', '#ff9900', '#ffff00',
                     '#00ff00', '#0099ff'][int(random(5))],
            'X': self.d * random(-0.15, 0.15),
            'Y': self.d * random(-0.15, 0.15),
            'd': self.d / random(2.5, 4)
            }
        self.propulsion = PVector(xspeed, yspeed)
        self.maxpropulsion = self.propulsion.mag()
        
    def display(self):
        # nucleus
        fill(self.nucleus['fill'])
        noStroke()
        circle(self.location.x + self.nucleus['X'], 
            self.location.y + self.nucleus['Y'],
            self.nucleus['d']
            )
        # cell membrane
        fill(0x880099ff)
        stroke('#ffffff')
        strokeWeight(3)
        r = self.d / 2.0
        cpl = r * 0.55
        cpx, cpy = self.circlePoint(frameCount/(r/2), r/8)
        xp, xm = self.location.x+cpx, self.location.x-cpx
        yp, ym = self.location.y+cpy, self.location.y-cpy
        beginShape()
        vertex(
               self.location.x, self.location.y-r # top vertex
               )
        bezierVertex(
                     xp+cpl, yp-r, xm+r, ym-cpl,
                     self.location.x+r, self.location.y # right vertex
                     )
        bezierVertex(
                     xp+r, yp+cpl, xm+cpl, ym+r,
                     self.location.x, self.location.y+r # bottom vertex
                     )
        bezierVertex(
                     xp-cpl, yp+r, xm-r, ym+cpl,
                     self.location.x-r, self.location.y # left vertex
                     )
        bezierVertex(
                     xp-r, yp-cpl, xm-cpl, ym-r,
                     self.location.x, self.location.y-r # (back to) top vertex
                     )
        endShape()
        
    def circlePoint(self, t, r):
        x = cos(t) * r
        y = sin(t) * r
        return [x,y]
