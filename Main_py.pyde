add_library('peasycam')
from Planet import Planet
    
sun = Planet('0xFF8C00', 50, loadImage('./Textures/sun.jpg'),)
mercury = Planet('0xCCCCCC', 8, loadImage('./Textures/mercury.jpg'), distance = 300, speed = 88, centerObject = sun)
venus = Planet('0xFFFF00', 18, loadImage('./Textures/venus.jpg'), distance = 400, speed = 225, centerObject = sun)
earth = Planet('0x0000FF', 20, loadImage('./Textures/earth.jpg'), distance = 500, speed = 365, centerObject = sun)
mars = Planet('0xDD0000', 10, loadImage('./Textures/mars.jpg'), distance = 600, speed = 686.7, centerObject = sun)
jupiter = Planet('0x8B8970', 30, loadImage('./Textures/jupiter.jpg'), distance = 700, speed = 778, centerObject = sun)
saturn = Planet('0xFFEBCD', 25, loadImage('./Textures/saturn.jpg'), distance = 800, speed = 10751, centerObject = sun)
uranus = Planet('0x97FFFF', 22, loadImage('./Textures/uranus.jpg'), distance = 900, speed = 30664, centerObject = sun)
neptune = Planet('0x4876FF', 21, loadImage('./Textures/neptune.jpg'), distance = 1000, speed = 60148, centerObject = sun)

moon = Planet('0x999999', 5, loadImage('./Textures/moon.jpg'), distance = 50,  speed = 29.57, centerObject = earth)

SolarSystem = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, moon]
def setup():
    size(1000, 1000, P3D)
    cam = PeasyCam(this, 1000)
    frameRate(40)
    
def draw():
    global sun
    global earth
    global angle
    global SolarSystem
    
    background(0)    
    for x in range(len(SolarSystem)):
        SolarSystem[x].show()
    
    delay(10)
    
    
    
    
