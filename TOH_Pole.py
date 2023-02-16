import turtle

class Pole(object):
    def __init__(self,name="",xpos=0,ypos=0,thick=10,length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
        
    def showpole(self):
        self.drawpole = turtle.Turtle()
        self.drawpole.speed(0)
        self.drawpole.hideturtle()
        self.drawpole.penup()
        self.drawpole.goto(self.pxpos, self.pypos)
        self.drawpole.pendown()
        self.drawpole.pensize(self.pthick)
        self.drawpole.forward(self.plength)
        self.drawpole.penup()
        self.drawpole.goto(self.pxpos, self.pypos + 20)
        self.drawpole.write(self.pname, align="center", font=("Arial", 16, "bold"))
        self.drawpole.goto(self.pxpos, self.pypos)
        
    def pushdisk(self,disk):
        self.stack.append(disk)
        self.toppos = self.toppos + 1
        disk.setpos(self.pxpos, self.pypos + self.toppos * 20)
        disk.showdisk()
        
    def popdisk(self):
        