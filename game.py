import pygame,sys,time
import common
from mapc import Map
from sprites.snake import Snake,Square

world = Map()
snakebod = pygame.sprite.Group()
player = Snake()
snakebod.add(player.head)
snakebod.add(player.tail)

class Game():
    def __init__(self):
        self.state = "menu"
        self.wason = [0,0]
        world.con_alp()
        player.head.ison = [x - .5 for x in world.spawn]
        self.someval = player.head.ison

    def gmloop(self):


        self.someval = player.head.ison
        if player.ismove and abs(player.head.dpos[0]) > common.valx*5 and abs(player.head.dpos[1]) > common.valy*5:
            print([(x,round(x)) for x in player.head.ison],player.head.dpos)
            world.updworld( [round(x) for x in player.head.ison] )
            player.head.dpos[0] = player.head.dpos[0]%common.valx if player.head.dpos[0] > 0 else -1*(abs(player.head.dpos[0])%common.valx)
            player.head.dpos[1] = player.head.dpos[1]%common.valy if player.head.dpos[1] > 0 else -1*(abs(player.head.dpos[1])%common.valy)
            print(player.head.ison,player.head.dpos)
            print()

        dx,dy = player.head.dpos
        world.mapblit(common.valx,common.valy,dx,dy)

        for event in pygame.event.get(): # for loop for events
            if event.type == pygame.QUIT: # quitting 
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player.add()
                    snakebod.add(player.tail.prev)
#                    player.head.d2pos = player.head.dpos.copy()
#                    world.updworld( player.head.ison )

                if event.key == pygame.K_SPACE and not player.ismove:
                    player.ismove = True
                elif event.key == pygame.K_SPACE and player.ismove:
                    player.ismove = False

                if event.key == pygame.K_d and (player.head.dir=="up" or player.head.dir == "down") and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "right"
                elif event.key == pygame.K_a and (player.head.dir=="up" or player.head.dir == "down")and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "left"
                elif event.key == pygame.K_w and (player.head.dir=="left" or player.head.dir == "right")and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "up"
                elif event.key == pygame.K_s and (player.head.dir=="left" or player.head.dir == "right")and common.time1 - player.timer > 0.5:
                    player.timer = common.time1
                    player.head.dir = "down"

        if player.ismove:
            snakebod.update(player.head.dmov[0],player.head.dmov[1])
            print(f'{player.head.ison},{self.wason},{player.head.dpos}, {player.head.d2pos }')

#        if (abs(player.head.d2pos[0]) > common.valx*5 or abs(player.head.d2pos[1]) > common.valy*5) and player.ismove:
#        if (abs(player.head.dpos[0]) > 18 and abs(player.head.dpos[0])) < 19 or (abs(player.head.dpos[1]) > 10 and abs(player.head.dpos[1]) < 11):
        if abs(self.wason[0] - player.head.ison[0]) == 5 or abs(self.wason[1] - player.head.ison[1]) == 5:
            print(f"happend {player.head.dpos}")
            player.head.d2pos = player.head.dpos.copy()
            world.updworld( player.head.ison )
            self.wason = player.head.ison.copy()
        
        snakebod.draw(common.vwin)
        pygame.draw.line(common.vwin,[0,0,0],common.displaymid,[common.displaymid[x] + player.head.d2pos[x] for x in range(2)])
        pygame.draw.line(common.vwin,[0,0,0],(0,common.displaymid[1]),(960,common.displaymid[1]))
        pygame.draw.line(common.vwin,[0,0,0],(common.displaymid[0],0),(common.displaymid[0],560))

    def menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quitting
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.state = "gmloop"
                    
    def selector(self): 
        if self.state == "gmloop":
            self.gmloop()
        elif self.state == "menu":
            self.menu()

