# -*- coding: utf-8 -*-
"""
Description
"""
#from scipy.special import expit
import numpy as np
pi = 3.1415926535898

WIDTH = 800
HEIGHT = 600
th_edge = np.arctan2(HEIGHT,WIDTH)

#TODO : fix/tune hardcoded numbers

class bullet():
    def __init__(self,vMax):
        th = np.random.uniform(-pi,pi) #random
        if th > -th_edge and th <= th_edge:
            x = WIDTH
            y = (HEIGHT+np.tan(th)*WIDTH)*0.5
        elif th > th_edge and th <= pi-th_edge:
            x = (WIDTH+HEIGHT/np.tan(th))*0.5
            y = HEIGHT
        elif th > th_edge-pi and th <= -th_edge:
            x = (WIDTH-HEIGHT/np.tan(th))*0.5
            y = 0
        else: 
            x = 0
            y = (HEIGHT-np.tan(th)*WIDTH)*0.5
        th += pi+np.random.uniform(-1.25,1.25) #about 0.4 pi
        v = vMax-np.random.choice(5)
        self.state = np.array([x,y,v*np.cos(th),v*np.sin(th)], dtype=int)
    
    def update(self):
        self.state[0:2] += self.state[2:4]
        
class game_body():
    vp = 7 #player speed
    def __init__(self):
        self.initialize()
        
    def initialize(self):
        self.rate = 0.3 #bullet spawning rate
        self.vMax = 10  #bullet speed #TODO make them vwrying over time (log?)
        self.t = 0
        self.bullets = []
        for i in range(15):  #Initial number of bullets
            self.bullets.append(bullet(self.vMax))
        self.x = int(WIDTH/2)
        self.y = int(HEIGHT/2)
    
    def update(self, u):
        #move player
        if u == 0:    #u = [up down left right stay]
            self.y = max(self.y-self.vp, 0)
        elif u == 1:
            self.y = min(self.y+self.vp, HEIGHT)
        elif u == 2:
            self.x = max(self.x-self.vp, 0)
        elif u == 3:
            self.x = min(self.x+self.vp, WIDTH)
        #move bullets
        for i in range(len(self.bullets)-1,-1,-1):
            b = self.bullets[i]
            b.update()
            d = b.state[0:2]-[self.x, self.y]
            if d.dot(d) < 20:
                return True #The game ends
            if (b.state[0] < 0) or (b.state[0] > WIDTH) or \
               (b.state[1] < 0) or (b.state[1] > HEIGHT):
                del self.bullets[i]
        #generate bullets:
        nb = np.random.poisson(self.rate)
        for i in range(nb):
            self.bullets.append(bullet(self.vMax))
        self.t += 1
        return False #The game proceeds
        