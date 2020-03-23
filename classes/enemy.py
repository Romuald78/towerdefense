
from ArcadeUtils import *

class Enemy:

    def __init__(self, pth, speed, power):
        self.path      = pth
        self.time      = 0
        self.totalTime = 100/speed          # speed should be between 1 and 100
        self.life      = power                 # power should be between 1 and 100
        self.sprite    = createSprite("./assets/images/enemy.png", (32,32), False)

    def hasReachedEndOfPath(self):
        return self.path.hasReachedEndOfPath(self.time/self.totalTime)

    def isDead(self):
        return self.life <= 0

    def getPosition(self):
        return (self.sprite.center_x,self.sprite.center_y)

    def getSprite(self):
        return self.sprite

    def shoot(self,damage):
        self.life -= damage

    def update(self,deltaTime):
        # update time of walking
        self.time += deltaTime
        # update position according to path
        x,y = self.path.getLerpPos(self.time/self.totalTime)
        self.sprite.center_x = x
        self.sprite.center_y = y


