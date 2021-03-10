from __future__ import division
class Planet:
    
    def __init__(self, farbe, groesse, Image, distance = 0, speed = 0, centerObject = None):
        self.farbe = farbe
        self.groesse = groesse
        self.distance = distance
        self.centerObject = centerObject
        self.angle = 0
        self.Image = Image
        
        if speed == 0:
            self.speed = 0
        else:
            self.speed = 360 / speed
        self.Currposition = PVector(float(0), float(self.distance), float(0))
    
    def show(self):
        if self.centerObject != None:
            
            stroke(0);
            strokeWeight(0);
            
            Ox = self.centerObject.Currposition.x - self.centerObject.Currposition.x
            Oy = self.distance 
            
            x = Ox * cos(radians(self.angle)) - Oy * sin(radians(self.angle))
            y = Ox * sin(radians(self.angle)) + Oy * cos(radians(self.angle))
            
            self.Currposition.x = x + self.centerObject.Currposition.x
            self.Currposition.y = y + self.centerObject.Currposition.y

            translate(self.Currposition.x, self.Currposition.y, self.Currposition.z)
            fill(self.farbe)
            
            #shape(self.globe)
            sphere(self.groesse)
            self.DrawOrbit()
            
            self.angle = self.angle + self.speed

        else:
            noFill();
            stroke(0);
            strokeWeight(0);
            fill(self.farbe)
            #shape(self.globe)
            sphere(self.groesse)
            
    def DrawOrbit(self):
        stroke('0xFFFFFF')
        strokeWeight(2)
        noFill()
        translate(-1 * self.Currposition.x, -1 * self.Currposition.y, 0)
        circle(self.centerObject.Currposition.x, self.centerObject.Currposition.y, self.distance * 2)
