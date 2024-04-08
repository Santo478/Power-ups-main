'''
Hola este es modulo game,
este modulo manejara la escena donde ocurre nuestro juego
'''
import random
import pygame
from pygame import mixer
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)
from .pausemenu import PauseMenu

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

'''cargar musica'''


'''background logic'''
background_image1 = pygame.image.load('assets//Backgrounds/RepeatBG.png').convert()
background_image = pygame.transform.scale(background_image1, (1000,700))

'''vidas'''

VidasPNG = pygame.image.load('assets/Extras/Heart.png').convert_alpha()
VidasPNG_scaled = pygame.transform.scale(VidasPNG, (40,40))


def StartScene(screen):
    background_scrolls = 0
    
    '''play music'''

    pygame.mixer.music.load('assets/audio/Music/8bitmusic.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1, 0, 1000)


    menu_sound = pygame.mixer.Sound('assets/audio/Sound/MenuSound.wav')
    menu_sound.set_volume(0.2)

    coin_pickup = pygame.mixer.Sound('assets/audio/Sound/CoinPick.wav')
    coin_pickup.set_volume(0.1)

    hurt_sound = pygame.mixer.Sound("assets/audio/Sound/Hurt.mp3")
    hurt_sound.set_volume(0.3)

    Power_pickup = pygame.mixer.Sound('assets/audio/Sound/PowerUP.wav')
    Power_pickup.set_volume(0.1)



    from elements.jorge import Player
    from elements.bug import Enemy
    from elements.intro import Coins
    from .death_screen import DeathScreen
    from elements.power_ups import PowerUp
    from elements.power_ups import SpeedPowerUp
    from elements.power_ups import ShieldPowerUp
    from elements.power_ups import SlownessPowerUp

    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()
    ''' 2.- generador de enemigos'''

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    ''' 3.- creamos la instancia de jugador'''
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    power_ups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    
    '''texto? tal vez'''
    puntaje = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    '''Zanax: Generador de Coins'''
    ADDCOIN = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCOIN, random.randint(7500,15000))

    '''Generador power ups'''

    POWERUP_TYPES = ["speed", "shield", "slowness"]

    def spawn_power_up():
<<<<<<< HEAD
        x = 1050
        y = random.randint(50, 650)
=======
        x = random.randrange(SCREEN_WIDTH)
        y = random.randrange(SCREEN_HEIGHT)
>>>>>>> f0b62e2566fc7e2c506c2e9ab491f058194c1448
        powerup_type = random.choice(POWERUP_TYPES)
        if powerup_type == "speed":
            powerup = SpeedPowerUp(x, y)
        elif powerup_type == "shield":
            powerup = ShieldPowerUp(x, y)
<<<<<<< HEAD
        elif powerup_type == "slowness":
=======
        elif powerup_type == "health":
>>>>>>> f0b62e2566fc7e2c506c2e9ab491f058194c1448
            powerup = SlownessPowerUp(x, y)
        power_ups.add(powerup)

    SPAWN_POWERUP_EVENT = pygame.USEREVENT + 3
<<<<<<< HEAD
    pygame.time.set_timer(SPAWN_POWERUP_EVENT, random.randint(1000,2000))
=======
>>>>>>> f0b62e2566fc7e2c506c2e9ab491f058194c1448

    ''' hora de hacer el gameloop '''
    running = True
    music_playing = False
    
    '''Animaciones'''
    from funciones.animations import SpriteSheet

    bug_sheet_image = pygame.image.load("assets/skins/bugs/BugSheet1.png").convert_alpha()
    jorge_sheet_image = pygame.image.load("assets/skins/Jorge/JorgeVJSheet.png").convert_alpha()
    coin_sheet_image = pygame.image.load('assets/Extras/IntroCoinsSheet.png').convert_alpha()
    sprite_sheets = [SpriteSheet(bug_sheet_image, 3, 100, 32, 32),
                    SpriteSheet(jorge_sheet_image, 2, 75, 50, 50),
                    SpriteSheet(coin_sheet_image, 8, 85, 30, 30)]

    for i in sprite_sheets:
        i.get_frames()
        i.last_update = pygame.time.get_ticks()

    frame_num = 0

    '''Loop principal'''

    while running:
        frame_num += 1
        retry = False
        if music_playing:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play(-1, 0, 1000)
            music_playing = True
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu_sound.play()
                    pause_state = PauseMenu(screen)
                    if pause_state == True:
                        
                        return
                    else:
                        pass

            elif event.type == QUIT:
                pygame.display.quit()
                pygame.quit()

            elif event.type == ADDENEMY:
                new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif puntaje >= 10:
                if event.type == ADDCOIN:
                    new_coins = Coins(SCREEN_WIDTH, SCREEN_HEIGHT)
                    coins.add(new_coins)
<<<<<<< HEAD
            
            elif event.type == SPAWN_POWERUP_EVENT:
                spawn_power_up()
                print('xd')
                

        for x in power_ups:
            screen.blit(x.image, x.rect)
=======
                
        if pygame.time.get_ticks() % random.randint(10000, 20000) == 0:
            spawn_power_up()
        
        for powerup in power_ups:
            screen.blit(powerup.image, powerup.rect)
>>>>>>> f0b62e2566fc7e2c506c2e9ab491f058194c1448

        #background scroller
        for i in range(2):
            screen.blit(background_image, (i * 1000 + background_scrolls, 0))
        background_scrolls -= 2
        if abs(background_scrolls) > 1000:
            background_scrolls = 0

        screen.blit(font.render(str(puntaje), True, (255,255,255), (0,0,0)), (0,0))

        #animacion sprite sheets
        for i in sprite_sheets:
            i.animate()


        if player.is_dead:
            if frame_num % 3 == 0:
                sprite_sheets[1].screen_blit(screen, player, 64)
        elif player.is_dead == False:
            sprite_sheets[1].screen_blit(screen, player, 64)
        for entity in enemies:
            sprite_sheets[0].screen_blit(screen, entity, entity.size)
        for coin in coins:
            sprite_sheets[2].screen_blit(screen, coin, 30)
            
        #actualizar objetos
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        for entity in coins:
            entity.update()
        for entity in enemies:
            score = entity.update()
            puntaje += score
<<<<<<< HEAD
        for entity in power_ups:
            entity.update()
=======
        power_ups.update()
>>>>>>> f0b62e2566fc7e2c506c2e9ab491f058194c1448

        #COLLIDE DE ENEMIGOS
        if player.is_dead == False:
            if pygame.sprite.spritecollide(player, enemies, False):   
                if pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask):
                    player.is_dead = True
                    player.lives -= 1
                    hurt_sound.play()
            
        if player.lives <= 0:
            player.kill()
            death = DeathScreen(screen)
            if death == True:
                StartScene(screen)
            elif death == False:
                from .main_menu import MainMenu
                MainMenu()
        #COLLIDE DE MONEDAS 
        if pygame.sprite.spritecollide(player, coins, False):   
            if pygame.sprite.spritecollide(player, coins, True, pygame.sprite.collide_mask):
                coin_pickup.play()
                puntaje += 500
        
        #COLLIDE DE POWER UPS

        collided_powerups = pygame.sprite.spritecollide(player, power_ups, True)
        for powerup in collided_powerups:
            if isinstance(powerup, SpeedPowerUp):
                powerup.apply_effect(player)
            elif isinstance(powerup, SlownessPowerUp):
                powerup.apply_effect(new_enemy)
            elif isinstance(powerup, ShieldPowerUp):
                powerup.apply_effect(player)

        #DISPLAY VIDAS
        for i in range(player.lives):
            screen.blit(VidasPNG_scaled,(820 + 40*i, 40))
        
        pygame.display.flip()
        clock.tick(40)


