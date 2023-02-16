import turtle

class Disk(object):
    def __init__(self,name="",xpos=0,ypos=0,height=20,width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        self.drawdisk = turtle.Turtle()
        #self.drawdisk.speed(0)
        self.drawdisk.hideturtle()
        self.drawdisk.penup()
        self.drawdisk.goto(self.dxpos, self.dypos)
        self.drawdisk.pendown()
        self.drawdisk.begin_fill()
        for i in range(2):
            self.drawdisk.forward(self.dwidth)
            self.drawdisk.left(90)
            self.drawdisk.forward(self.dheight)
            self.drawdisk.left(90)
        self.drawdisk.end_fill()
        
    def newpos(self,xpos,ypos):
        self.dxpos = xpos
        self.dypos = ypos
        
    def cleardisk(self):
        self.drawdisk.clear()
        self.drawdisk.reset()