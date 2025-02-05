import pgzrun
from pgzero.builtins import *
from settings import *

n_stage = 0

#Itens for game
class Obj(Actor):
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos)

        self.topleft = pos
        self.name = None
        self.group = groups
        for g in self.group:
            if g is not None:
                g.append(self)
        
    def update(self):
        
        pass

class Saw(Obj):
    def __init__(self, img, pos, *group):
        super().__init__(img, pos, *group)

        self.limit = 200
        self.start_pos = self.x
        self.speed = 1
        self.min = self.start_pos
        self.max = self.start_pos + self.limit

    def move(self):
        self.start_pos -= self.speed
        
        if self.start_pos < self.min:
            self.speed *= -1
        elif self.start_pos > self.max:
            self.speed *= -1
        
        animate(self, pos=(self.start_pos, self.y))

    def update(self):
        self.angle += 3
        self.move()
        
class Bg_animated(Actor):
    def __init__(self,img, y):
        super().__init__(img)

        self.y = y

    def update(self, speed, limit, start_position):
        self.y += speed
        if self.y >= limit:
            self.y = start_position

class Button(Obj):
    def __init__(self, img, pos, group):
        super().__init__(img, pos, group)
    
    def update(self):
        pass

class Fade:
    def __init__(self, group):
        
        
        self.image = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        self.image.fill(COLOR_BG)
        self.image.set_alpha(255)
        self.rect = self.image.get_rect(topleft=(0,0))

        self.alpha = 255
        self.speed = 10
        self.on = True
        self.call_fade = False

        self.group = group
        self.group.append(self)
    
    def change_scenes(self, new_scene):
        self.new_scene = new_scene

    def fadein(self):
        self.on = True
        self.call_fade = True

    def update(self):
        if self.call_fade:
            if self.on:
                if self.alpha > 0:
                    self.alpha -= self.speed
                    self.image.set_alpha(self.alpha)
                else:
                    self.call_fade = False
            else:
                if self.alpha < 255:
                    self.alpha += self.speed
                    self.image.set_alpha(self.alpha)
                else:
                    self.call_fade = False

    def draw(self):
        screen.blit(self.image, self.rect)

class Player(Obj):
    def __init__(self, img, pos, collisions, group):
        super().__init__(img, pos, group)
        
        self.life = 3
        self.start_position = (0, 0)
        self.speed = 5
        self.jump_speed = -18
        self.gravity = 1
        
        self.direction = Vector2(0, 0)
        self.collisions = collisions
        
        self.image = 'player/base/base'
        self.collision_area = Rect(self.x, self.y, 40,40)
        
        self.on_ground = False
        self.can_atack = False
        self.time_atack = 0

        self.animations = {
            State.IDLE: Animated_sprite('player/idle/', 7),
            State.WALK: Animated_sprite('player/walk/', 7),
            State.JUMP: Animated_sprite('player/jump/', 5),
            State.ATACK: Animated_sprite('player/atack/', 5),
        }
        
        self.control_animation = self.animations[State.IDLE]
        self.current_animation = State.IDLE

        

    def apply_jump(self):
        if self.on_ground:
            self.direction.y += self.jump_speed
    
    def return_to_start(self):
        self.x, self.y = self.start_position

    def drop_platform(self):
        if self.y > HEIGHT:
            self.return_to_start()

    def y_collision_check(self):
        for sprite in self.collisions:
            if sprite.name == "platform":
                if sprite.colliderect(self):
                    if self.direction.y > 0:
                        self.direction.y = 0
                        self.bottom = sprite.top
                        self.on_ground = True
                    if self.direction.y < 0:
                        self.direction.y = 0
                        self.top = sprite.bottom
    
    def x_collision_check(self):
    
        for sprite in self.collisions:
            if sprite.name == "platform":
                if sprite.colliderect(self):
                    if self.direction.x > 0:
                        self.right = sprite.left
                    if self.direction.x < 0:
                        self.left = sprite.right
    
    def gravity_force(self):
        
        self.direction.y += self.gravity
        self.y += self.direction.y
    
    def move(self):
        self.x += self.direction.x * self.speed
    
    def reset_atack(self, atack_speed=20):
        if self.can_atack:
            self.time_atack += 1
            if self.time_atack >= atack_speed:
                self.can_atack = False
                self.time_atack = 0
                
    def events(self):
        if keyboard.left:
            self.direction.x = -1
        elif keyboard.right:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
        if keyboard.up and self.on_ground:
            self.on_ground = False
            self.direction.y = self.jump_speed
        
        if keyboard.z:
            self.can_atack = True
            
    def animation_stage(self):
        # Altera o estado baseado nas condições do jogador
        if self.can_atack:
            self.current_animation = State.ATACK
        else:

            if self.on_ground and self.direction.x != 0:
                self.current_animation = State.WALK
            elif self.on_ground and self.direction.x == 0:
                self.current_animation = State.IDLE
            elif not self.on_ground:
                self.current_animation = State.JUMP
        
        # Se a animação atual for diferente, mude para a animação correspondente
        if self.control_animation != self.animations[self.current_animation]:
            self.control_animation = self.animations[self.current_animation]

    def draw(self):
        overlay_image = self.control_animation.animation()
        screen.blit("player/base/base", (self.x - 20,self.y - 20))
        screen.blit(overlay_image, (self.x - 30, self.y - 20))

    def update(self):
        self.events()
        self.move()
        self.x_collision_check()
        self.gravity_force()
        self.y_collision_check()
        self.animation_stage()
        self.reset_atack()
        self.drop_platform()


#Scenes Objs
class Scene:

    def __init__(self):

        self.new = self
        self.all_sprites = []
        self.collisions = []

        self.world_map = [MAP0, MAP1, MAP2]
        self.stage_map = 0

    def start_music(self, lib, music):
        lib.play(music)
    
    def draw(self, screen):
        pass

    def generate_bg(self, all_sprites):
        list_img = ["titles/1.png","titles/2.png","titles/3.png"]
        for row_index, row in enumerate(BG_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if col == "X":
                    new = Obj('tiles/bg', (x,y), all_sprites)
                

    def generate_map(self, all_sprites, collisions, player):
        list_img = ["titles/1.png","titles/2.png","titles/3.png"]
        for row_index, row in enumerate(self.world_map[n_stage]):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                choose = random.choice(list_img)
                if col == "X":
                    new = Obj(choose, (x,y), all_sprites, collisions)
                    new.name = "platform"
                elif col == "C":
                    new = Obj('titles/4', (x,y), all_sprites, collisions)
                    new.name = "next"
                elif col == "O":
                    new = Saw('obstacles/o', (x,y), all_sprites, collisions)
                    new.name = "obstacle"
                elif col == "S":
                    new = Obj('obstacles/o2', (x+16,y+32), all_sprites, collisions)
                    new.name = "obstacle"
                elif col == "P":
                    player.x, player.y = x,y
                    player.start_position = (x,y)
            
    def on_mouse_down(self, pos):
        pass

    def on_key_down(self, key):
        pass

    def update(self):
        pass
    
    def change_scene(self, new_scene):
        self.new = new_scene
    
class MenuScene(Scene):
    def __init__(self):
        super().__init__()

        self.all_sprites = []

        self.menu_itens = {
        'bg1' : Bg_animated('menu/bg', 360),
        'bg2' : Bg_animated('menu/bg', -360),
        'bg_border' : Obj('menu/bg_mol', (0,0),self.all_sprites),
        'title' : Obj('menu/title', (WIDTH / 2 - 230 , HEIGHT / 2 - 300),self.all_sprites),
        'button_play' : Button('menu/text_start', (WIDTH / 2 - 57, HEIGHT / 2 + 50),self.all_sprites),
        'button_exit' : Button('menu/text_exit', (WIDTH / 2 - 57, HEIGHT / 2 + 150),self.all_sprites)
        }

        
        self.fade = Fade(self.all_sprites)
        self.fade.fadein()

        self.start_music(music, 'menu')

    def draw(self, screen):

        self.menu_itens['bg1'].draw()
        self.menu_itens['bg2'].draw()
        for sprite in self.all_sprites:
            sprite.draw()
        
    def on_key_down(self,key):
        
        if key == 27: #ESC
            quit()
        if key == 13: #ENTER
            self.start_music(music, 'game')
            self.change_scene(GameScene())

    def on_mouse_down(self, pos):
        if self.menu_itens['button_play'].collidepoint(pos):
            self.start_music(music, 'game')
            self.change_scene(GameScene())
        elif self.menu_itens['button_exit'].collidepoint(pos):
            quit()

    def update(self):

        self.menu_itens['bg1'].update(speed=1, limit=1080, start_position=360)
        self.menu_itens['bg2'].update(1,360,-360)
        for sprite in self.all_sprites:
            sprite.update()

class GameScene(Scene):
    def __init__(self):
        super().__init__()

        self.all_sprites = []
        self.all_collisions = []

        self.generate_bg(self.all_sprites)
        self.player = Player('player/idle/0.png', (100,0),self.all_collisions, self.all_sprites)
        self.generate_map(self.all_sprites, self.all_collisions, self.player)

        self.fade = Fade(self.all_sprites)
        self.fade.fadein()

        

    def draw(self, screen):
        screen.fill(COLOR_BG)
        for sprite in self.all_sprites:
            sprite.draw()

    def on_key_down(self, key):
        pass

    def on_mouse_down(self, pos):
        pass

    def check_collision(self):
        global n_stage
        for sprite in self.all_collisions:
            if sprite.name == "next":
                if sprite.colliderect(self.player):
                    n_stage += 1
                    self.change_scene(GameScene())
                    
                    
            if sprite.name == "obstacle":
                if sprite.colliderect(self.player):
                    if self.player.life > 1:
                        self.player.life -= 1
                        self.player.return_to_start()
                    else:
                        self.change_scene(GameOver())
        

    def update(self):
        for sprite in self.all_sprites:
            sprite.update()
        
        self.check_collision()
        
class GameOver(Scene):
    def __init__(self):
        super().__init__()

        print("gameover")
        self.start_music(music, 'gameover')

TITLE = "Battle Castle"

current_scene = MenuScene()

def on_key_down(key):
    current_scene.on_key_down(key)

def on_mouse_down(pos):
    current_scene.on_mouse_down(pos)

def draw():
    screen.fill(COLOR_BG)
    current_scene.draw(screen)

def update():
    global current_scene
    current_scene.update()
    current_scene = current_scene.new
    
pgzrun.go()
