import arcade
from ArcadeUtils import *
import math
import random

class Tower:

    def __init__(self, towerType, x0, y0, cellSize, enemyList):
        # create sprite according to type
        self.sprite = createSprite("./assets/images/tower"+towerType+".png",(cellSize),True)
        self.sprite.center_x = x0
        self.sprite.center_y = y0
        self.sprite.angle    = random.randint(0,360)
        self.range           = 300
        self.power           = 0.01
        self.enemies         = enemyList
        self.readyToShoot    = False
        self.hasTarget       = False
        self.lastTarget      = None

    def __getDist2(self,pos):
        dx = self.sprite.center_x - pos[0]
        dy = self.sprite.center_y - pos[1]
        return dx*dx + dy*dy

    def getPos(self):
        return (self.sprite.center_x, self.sprite.center_y)

    def getSprite(self):
        return self.sprite

    def update(self,deltaTime):
        # init flags
        self.hasTarget    = False
        self.readyToShoot = False
        # check if we have some enemies to shoot
        if len(self.enemies) > 0:
            nearest = self.enemies[0].getPosition()
            minDist = self.__getDist2(nearest)
            tmpTrgt = self.enemies[0]
            # get nearest enemy from the list
            for e in self.enemies:
                p = e.getPosition()
                d = self.__getDist2(p)
                if d<minDist:
                    nearest = p
                    minDist = d
                    tmpTrgt = e
            # check if minDist is in the range
            if minDist <= self.range*self.range:
                self.hasTarget = True
                # compute enemy angle
                dx = nearest[0]-self.sprite.center_x
                dy = nearest[1]-self.sprite.center_y
                ang  = math.atan2(dy,dx) * 180 / math.pi
                ang += 360
                ang %= 360
                # check if we are in the fire angle
                diff = (self.sprite.angle-ang+360+180)%360
                if abs(diff-180) < 10:
                    self.sprite.angle = ang
                    self.readyToShoot = True
                    self.lastTarget   = tmpTrgt
                elif diff-180 > 0:
                    self.sprite.angle -= 60 * deltaTime * 4
                else:
                    self.sprite.angle += 60 * deltaTime * 4

        if not self.hasTarget:
            # just turn around waiting for a target
            self.sprite.angle += 60*deltaTime * 1

        if self.readyToShoot:
            self.lastTarget.shoot(self.power)

    def drawShoot(self):
        if self.readyToShoot:
            x0    = self.sprite.center_x
            y0    = self.sprite.center_y
            x1,y1 = self.lastTarget.getPosition()
            arcade.draw_line(x0,y0,x1,y1,(255,0,0,128),3)