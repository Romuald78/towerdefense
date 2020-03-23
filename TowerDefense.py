### ====================================================================================================
### IMPORTS
### ====================================================================================================
import arcade
from ArcadeUtils import *
from random import *
import time
from classes.player import *
from classes.path import *
from classes.enemy import *

TILE_SIZE = 80
NB_CELLS_X = 1820//TILE_SIZE
NB_CELLS_Y = 980//TILE_SIZE
SCREEN_WIDTH  = NB_CELLS_X*TILE_SIZE
SCREEN_HEIGHT = NB_CELLS_Y*TILE_SIZE
var = Variables()



### ====================================================================================================
### YOUR OWN FUNCTIONS HERE
### ====================================================================================================
def createNewEnemy():
    enmy = Enemy(var.path, 5, 1)
    var.enemies.append(enmy)
    var.enemySpriteList.append(enmy.getSprite())


### ====================================================================================================
### INITIALISATION OF YOUR VARIABLES
### ====================================================================================================
def setup():
    # init path
    var.path = Path( (TILE_SIZE,TILE_SIZE), NB_CELLS_X, NB_CELLS_Y )
    # init players
    var.players = []
    # init enemies
    var.enemies = []
    var.enemySpriteList = arcade.SpriteList()



### ====================================================================================================
### UPDATE OF YOUR GAME DATA
### ====================================================================================================
def update(deltaTime):
    # update path
    var.path.update(deltaTime)
    # update players
    for p in var.players:
        p.update(deltaTime)
    # update enemies
    for e in var.enemies:
        e.update(deltaTime)
        if e.hasReachedEndOfPath() or e.isDead():
            var.enemies.remove(e)
            var.enemySpriteList.remove(e.getSprite())

### ====================================================================================================
### DRAW YOUR IMAGES ON THE SCREEN
### ====================================================================================================
def draw():
    # draw all path
    var.path.draw()
    # draw all players
    for p in var.players:
        p.draw()
    # draw all enemies
    var.enemySpriteList.draw()


### ====================================================================================================
### FUNCTION CALLED WHEN YOU PRESS A KEY ON THE KEYBOARD
### ====================================================================================================
def onKeyEvent(key,isPressed):
    pass



### ====================================================================================================
### FUNCTION CALLED WHEN YOU PRESS A BUTTON ON A GAMEPAD CONTROLLER
### ====================================================================================================
def onButtonEvent(gamepadNum,buttonNum,isPressed):
    # if start is pressed, add a player (if not already added)
    if buttonNum == 7 and not isPressed:
        for p in var.players:
            if p.getGamepadID() == gamepadNum:
                return
        # add player
        newPlayer = Player(gamepadNum, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), (SCREEN_WIDTH, SCREEN_HEIGHT), (TILE_SIZE, TILE_SIZE))
        var.players.append( newPlayer )
        # debug paint Towers all over the map for perf tests
        #for i in range(NB_CELLS_X):
        #    for j in range(NB_CELLS_Y):
        #        newPlayer.createTower(i*TILE_SIZE, j*TILE_SIZE, var.enemies)

    # for enemy creation
    elif buttonNum == 6 and not isPressed:
        createNewEnemy()

    # for other player buttons
    else:
        # check if a player is registered
        for p in var.players:
            if p.getGamepadID() == gamepadNum:
                # process button A to create a tower
                if buttonNum == 0 and not isPressed:
                    # get player cursor position
                    tilePos = p.getCursorTilePos()
                    p.createTower(tilePos[0],tilePos[1], var.enemies)

### ====================================================================================================
### FUNCTION CALLED WHEN YOU MOVE AN AXIS ON A GAMEPAD CONTROLLER
### ====================================================================================================
def onAxisEvent(gamepadNum,axisName,analogValue):
    # check if gamepad is registered
    for p in var.players:
        if p.getGamepadID() == gamepadNum:
            if axisName == "x":
                if abs(analogValue) >= 0.25:
                    var.players[0].moveX(analogValue)
                else:
                    var.players[0].moveX(0)
            if axisName == "y":
                if abs(analogValue) >= 0.25:
                    var.players[0].moveY(-analogValue)
                else:
                    var.players[0].moveY(0)
            return


