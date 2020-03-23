from ArcadeUtils import *
from classes.tower import *

NONE  = 0x00
LEFT  = 0x01
RIGHT = 0x02
UP    = 0x04
DOWN  = 0x08

class Player:

    def __init__(self, ctrlID, initPos, viewDim, cellSize):
        self.gamepadID  = ctrlID
        self.towers     = []
        self.towerSpriteList = arcade.SpriteList()
        self.screenDim  = viewDim
        self.tileSize   = cellSize
        self.moveSpeeds = [0,0]
        target = createSprite("./assets/images/target.png", (32,32), False)
        self.cursor     = [initPos[0],initPos[1],target]

    def __updateCursor(self,deltaTime):
        # get data
        x, y, s = self.cursor
        dx      = self.moveSpeeds[0]
        dy      = self.moveSpeeds[1]
        # update cursor position
        x = min(max(x + dx*60*deltaTime*10, 0), self.screenDim[0])
        y = min(max(y + dy*60*deltaTime*10, 0), self.screenDim[1])
        # update sprite position according to the grid
        s.center_x = x
        s.center_y = y
        # set data
        self.cursor = [x,y,s]

    def getGamepadID(self):
        return self.gamepadID

    def getCursorTilePos(self):
        return (self.cursor[2].center_x,self.cursor[2].center_y)

    def createTower(self,x0,y0,enemies):
        # check x0 and y0 are centered on a tile
        x0  = (x0 // self.tileSize[0]) * self.tileSize[0]
        y0  = (y0 // self.tileSize[1]) * self.tileSize[1]
        x0 += self.tileSize[0] / 2
        y0 += self.tileSize[1] / 2
        twr = Tower("ABC"[random.randint(0,2)],x0,y0,self.tileSize,enemies)
        self.towers.append( twr )
        self.towerSpriteList.append( twr.getSprite() )

    def moveX(self,value):
        self.moveSpeeds[0] = value

    def moveY(self,value):
        self.moveSpeeds[1] = value

    def update(self,deltaTime):
        # update cursor
        self.__updateCursor(deltaTime)
        # update towers
        for t in self.towers:
            t.update(deltaTime)

    def draw(self):
        # draw cursor (get tile position first)
        # tileX = (self.cursor[0]//self.tileSize[0])*self.tileSize[0] + self.tileSize[0]/2
        # tileY = (self.cursor[1]//self.tileSize[1])*self.tileSize[1] + self.tileSize[1]/2
        # arcade.draw_rectangle_filled(tileX, tileY, self.tileSize[0], self.tileSize[1], (255,255,255,32) )
        self.cursor[2].draw()
        # draw towers
        self.towerSpriteList.draw()

        # TODO improve drawings of shots (using SpriteList)
        # Draw lasers from towers
        #for t in self.towers:
        #    t.drawShoot()
