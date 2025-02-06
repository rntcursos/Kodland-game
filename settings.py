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

TEXT_INTRO = """
Título: O Cavaleiro e a Armadilha do Mago Tharos

Era uma vez, um valente cavaleiro chamado Sir Alaric. Ele era conhecido por sua bravura e lealdade,
mas seu coração estava pesado com a dor da perda.
Sua filha, a doce e corajosa Elenora, havia sido sequestrada por um temido mago chamado Tharos, que habitava um castelo
sombrio nas montanhas.

Determinado a resgatar sua filha, Sir Alaric armou-se com sua armadura reluzente e sua espada afiada. 
Ele montou seu fiel cavalo, um magnífico corcel chamado Tempestade, e partiu em direção ao castelo.

Após dias de viagem, ele finalmente chegou às imponentes portas de ferro do castelo de Tharos.
Com um golpe firme, ele empurrou as portas e entrou. O interior do castelo era tão escuro quanto
a noite, com paredes de pedra cobertas de musgo e teias de aranha. Sir Alaric chamou por Elenora,
mas apenas o eco de sua própria voz respondeu. Ele avançou cautelosamente, sentindo que algo estava errado.

De repente, as portas se fecharam atrás dele com um estrondo, e uma risada sinistra ecoou pelas paredes.
Era Tharos, que apareceu em uma nuvem de fumaça negra. "Bem-vindo, Sir Alaric! Você caiu na minha armadilha.
Sua coragem é admirável, mas você nunca sairá daqui!"

Sir Alaric, percebendo que estava preso, não se deixou abater.
Ele sabia que precisava encontrar uma saída antes de poder resgatar sua filha...

Continua!
"""