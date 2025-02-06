from pgzero.screen import *
import random

#utils
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class State:
    IDLE = 1
    WALK = 2
    JUMP = 3
    DASH = 4
    DASH_LEFT = 5
    WALK_LEFT = 6
    JUMP_LEFT = 7
    IDLE_LEFT = 8

class Animated_sprite:

    def __init__(self, path, n_frame, speed_animation=5):
        
        self.path = path
        self.n_frame = n_frame
        self.speed_animation = speed_animation

        self.time = 0
        self.frame = 0
    
    def animation(self):
        self.time += 1
        if self.time > self.speed_animation:
            self.time = 0
            self.frame = (self.frame + 1) % self.n_frame
            
        return f'{self.path}{self.frame}.png'



#Screen settings
WIDTH = 1280
HEIGHT = 720

#COLORS
COLOR_BG = (20,20,30)


TILE_SIZE = 64

BG_MAP = [
    'XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX', 
]

MAP0 = [
    'XXXX XXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXX XXXXX',
    'XXXX XXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',
    '                    ',
    '                    ',
    ' P   AAAAAA       C  ',
    'XXXXXXXXXXX  XXXXXXX',
    'XXXXXXXXXXX  XXXXXXX',
    'XXXXXXXXXXX  XXXXXXX',
    'XXXXXXXXXXXSSXXXXXXX',
    'XXXXXXXXXXXXXXXXXXXX',

]

MAP1 = [
'XXXX XXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXX XXXXX',
'XXXXXXXXXXXXXXXXXXXX',
'     XXXXXXXXXXXXXXX',
'      XXXXXXXXXXXXXX',
'       XXXXXXXXXXXXX',
'                    ',
'                    ',
'  P   AA   A       C',
'XXXXX XX  XXX XX  XXX',
'XXXXX XX  XXX XX  XXX',
'XXXXX XX  XXX XX  XXX',
'SSSSSSSSSSSSSSSSSSSSS']

MAP2 = [
'                    ',
'                    ',
'                    ',
'                    ',
'                    ',
'                    ',
'            X       ',
'                    ',
'     X        XAAAXXX',
'  PX XX     XAXX  C  ',
'X XX  X XXAAX XXXXXXX',
'X XX  X XX  X XXXXXXX',
'SSSSSSSSSSSSSSSSSSSSS']

MAP3 = [
'                    ',
'                    ',
'                    ',
'                    ',
'                    ',
'                    ',
'                  C ',
'          XXX     XX',
'       X  XXXX    XX',
'  P XSSSSSSSSSSSSSSS',
'XXXXXXXXXXXXXXXXXXXX']

MAP4 = [
'XXXXXXXXXXXXXXXXXXXX',
'XXXXXXXXXXXXXXXXXXXX',
'                    ',
'                    ',
'                    ',
'                    ',
'            O     C ',
'  O       XXXX    XX',
'       X  XXXX    XX',
'  P   XXSSXXXX    XX',
'SXXXXXXXXXXXXXSSSSXX']

