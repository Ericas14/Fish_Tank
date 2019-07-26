from random import *
def setup():
    size(600,600)
    background(59, 34, 245)
    fishy(300,200)
    
    f = 0
    while f <= 30:
        fishy(randint(0,600), randint(0,600))
        f = f + 1
    i = 0
    while i <= 30:
        fishy2(randint(0,600), randint(0,600))
        i = i + 1 
def fishy2(x ,y):
    # x = 300
    # y = 300
    fill(randint(0,255), randint(0,255), randint(0,255))
    noStroke()
    ellipse(x,y,100,50)
    triangle(x + 65, y + 20, x + 45, y ,x + 65, y - 20)
    
    
def fishy(x2, y2):
    #x2 = 40
    #y2 = 100
    fill(randint(0,255), randint(0,255), randint(0,255))
    triangle(x2, y2, x2 - 20, y2 - 15, x2, y2 - 30)
    fill(255,255,255)
    triangle(x2, y2, x2 + 20, y2 - 15, x2, y2 - 30)
    fill(randint(0,255), randint(0,255), randint(0,255))
    triangle(x2 + 20 , y2- 15, x2, y2 - 30, x2 + 20, y2 - 45)
    triangle(x2 + 20, y2 + 15, x2, y2, x2 + 20, y2 - 15)
    triangle(x2 + 40, y2, x2 + 20, y2 - 15, x2 + 40, y2 - 30)
    fill(0,0,0)
    ellipse(x2 - 5, y2 - 15, 5 ,5)





    
