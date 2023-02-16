import turtle


class Pole(object):

    def __init__(self, name = "", xpos = 0, ypos = 0, thick = 10, length = 100):
        self.pname = name
        self.stack = []
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
        self.drawpole.write(
            self.pname, align = "center", font = ("Arial", 16, "bold")
        )
        self.drawpole.goto(self.pxpos, self.pypos)

    def pushdisk(self, disk):
        print(self.stack)
        self.stack.append(disk)
        disk.newpos(self.pxpos, self.pypos + len(self.stack) * 20)
        disk.showdisk()
        print(self.stack)

    def popdisk(self):
        print(self.stack)
        return self.stack.pop()