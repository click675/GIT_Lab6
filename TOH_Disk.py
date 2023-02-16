import turtle


class Disk(object):

    def __init__(self, name = "", xpos = 0, ypos = 0, height = 20, width = 40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.drawdisk = turtle.Turtle()

    def showdisk(self):
        self.drawdisk.speed(0)
        self.drawdisk.hideturtle()
        self.drawdisk.penup()
        self.drawdisk.goto(self.dxpos, self.dypos)
        self.drawdisk.pendown()
        self.drawdisk.begin_fill()
        self.drawdisk.forward(self.dwidth)
        self.drawdisk.left(90)
        self.drawdisk.forward(self.dheight)
        self.drawdisk.left(90)
        self.drawdisk.forward(self.dwidth * 2)
        self.drawdisk.left(90)
        self.drawdisk.forward(self.dheight)
        self.drawdisk.left(90)
        self.drawdisk.forward(self.dwidth)
        self.drawdisk.left(90)
        self.drawdisk.end_fill()
        self.drawdisk.penup()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos
        self.cleardisk()
        self.showdisk()

    def cleardisk(self):
        self.drawdisk.clear()
        self.drawdisk.reset()