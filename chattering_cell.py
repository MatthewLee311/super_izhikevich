import izhikevich_cells as izh

class cCell(izh.izhCell):
    def __init__(self,stimVal):
        super().__init__(stimVal)
        self.celltype='Chattering Cell'
        self.C=50
        self.k=1.5
        self.b=1
        self.vpeak=25
        self.d=150

def createCell():
    myCell = cCell(stimVal=4000)
    myCell.simulate()
    izh.plotMyData(myCell)

if __name__=='__main__':
    createCell()
