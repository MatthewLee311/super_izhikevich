import izhikevich_cells as izh

class ibCell(izh.izhCell):
    def __init__(self,stimVal):
        super().__init__(stimVal)
        self.celltype='Intrinsically Bursting Cell'
        self.C=150
        self.k=1.2
        self.vr=-75
        self.vt=-45
        self.a=0.01
        self.b=5
        self.vpeak=50
        self.d=130

def createCell():
    myCell = ibCell(stimVal=4000)
    myCell.simulate()
    izh.plotMyData(myCell)

if __name__=='__main__':
    createCell()
