import TOH_Disk, TOH_Pole

class Hanoi(object):
    def __init__(self,n=3,start="A",workspace="B",destination="C"):
        self.startp = TOH_Pole.Pole(start,0,0)
        self.workspacep = TOH_Pole.Pole(workspace,150,0)
        self.destinationp = TOH_Pole.Pole(destination,300,0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdisk(TOH_Disk.Disk("d"+str(i),0,i*150,20,(n-i)*30))
            
        def move_disk(self,start,destiantion):
            disk = start.popdisk()
            destiantion.pushdisk(disk)
            
        def move_tower(self,m,s,d,w):
            if n == 1:
                self.move_disk(s,d)
            else:
                self.move_tower(n-1,s,w,d)
                self.move_disk(s,d)
                self.move_tower(n-1,w,d,s)
                
        def solve(self):
            self.move_tower(3,self.startp,self.workspacep,self.destinationp)

h = Hanoi()
h.solve()