# -*- coding: utf-8 -*-
"""
Description
"""
from PyQt4 import QtGui, QtCore
import sys
import pydodge

dt = 30    #somehow relate to the rate of spawning

class gui(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(pydodge.WIDTH,pydodge.HEIGHT)
        self.move(400,300)
        self.setWindowTitle('PyDodge')
                
        self.colorb = QtGui.QColor(0,70,170)
        self.colorp = QtGui.QColor(170,70,0)
        self.rp = 4    #radius player
        self.rb = 3    #radius bullet
    
        self.show()
        self.t = 0
        self.gaming = False
        self.game = pydodge.game_body()
        
    def new_game(self):
        self.gaming = True
        self.game.initialize()
        self.u = 4
        self.t = 0
        self.tid = self.startTimer(dt)
                
    def keyPressEvent(self,e):
        if not self.gaming: self.new_game()
        if e.key() == QtCore.Qt.Key_W:    #consider dictionary? 
            self.u = 0
        elif e.key() == QtCore.Qt.Key_S:
            self.u = 1
        elif e.key() == QtCore.Qt.Key_A:
            self.u = 2
        elif e.key() == QtCore.Qt.Key_D:
            self.u = 3
        elif e.key() == QtCore.Qt.Key_Up:
            self.u = 0
        elif e.key() == QtCore.Qt.Key_Down:
            self.u = 1
        elif e.key() == QtCore.Qt.Key_Left:
            self.u = 2
        elif e.key() == QtCore.Qt.Key_Right:
            self.u = 3
            
        
    def keyReleaseEvent(self,e): #TODO: but when there are multiple inputs
        self.u = 4
    
    def timerEvent(self,e):
        self.t += dt
        if self.game.update(self.u):
            self.killTimer(self.tid)
            self.gaming = False
        self.update()
        
    def mousePressEvent(self, e):
        if not self.gaming: self.new_game()
        
    def paintEvent(self,e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawText(10,20,'{:.2f}'.format(self.t/1000))
        qp.drawText(pydodge.WIDTH-25,20,'{:3d}'.format(len(self.game.bullets)))
        qp.setPen(self.colorp)
        qp.setBrush(self.colorp)
        qp.drawEllipse(self.game.x-self.rp,self.game.y-self.rp,2*self.rp,2*self.rp)
        qp.setPen(self.colorb)
        qp.setBrush(self.colorb)
        for b in self.game.bullets:
            qp.drawEllipse(b.state[0]-self.rb, b.state[1]-self.rb,2*self.rb,2*self.rb)
        qp.end()

def main():
    app = QtGui.QApplication(sys.argv)
    _ = gui()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
