import arcade
from ArcadeUtils import *


class Path:

    def __init__(self, cellSize, nbCellX, nbCellY):
        print(cellSize,nbCellX, nbCellY)
        # create sprite according to type
        self.sprites = self.__createRandomPath(cellSize,nbCellX, nbCellY)

    def __createRandomPath(self, cellSize, nbCellX, nbCellY):
        cells = []
        for x in range(1,nbCellX-1):
            cells.append( (x,1) )
        for y in range(2, nbCellY - 2):
            cells.append((nbCellX - 2, y))
        for x in range(nbCellX-2,0,-1):
            cells.append( (x,nbCellY-2) )
        # pathSprites
        pathSpr = []
        for c in cells:
            s = createSprite("./assets/images/path01.png",(cellSize), False)
            s.center_x = c[0]*cellSize[0]+(cellSize[0]/2)
            s.center_y = c[1]*cellSize[1]+(cellSize[1]/2)
            pathSpr.append(s)
        return pathSpr

    def getLength(self):
        return len(self.sprites)

    def hasReachedEndOfPath(self,x0):
        pos = self.getLerpPos(x0)
        return (pos[0] == self.sprites[-1].center_x) and (pos[1] == self.sprites[-1].center_y)

    def getLerpPos(self,x0):
        # floor to 0
        x0 = max(0,x0)
        # set index value
        x0 *= len(self.sprites)
        # ceiling to len(self.sprites)-1
        x0 = min(x0, len(self.sprites)-1)
        # get index
        a = int(x0)
        b = a+1
        # if end of the path, just send the last position
        if a == len(self.sprites)-1:
            b = a
        # get X and Y values
        xA = self.sprites[a].center_x
        xB = self.sprites[b].center_x
        yA = self.sprites[a].center_y
        yB = self.sprites[b].center_y
        # get ratio
        r = x0 - a
        x = xA * (1 - r) + xB * (r)
        y = yA * (1 - r) + yB * (r)
        return (x,y)

    def update(self,deltaTime):
        pass

    def draw(self):
        for s in self.sprites:
            s.draw()

