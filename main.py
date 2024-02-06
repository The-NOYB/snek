import pygame,math,sys,time,csv
import common,game
from sprites.snake import Snake,Square

pygame.init()
fontt = pygame.font.Font(None,size=48)
window = pygame.display.set_mode(common.displaysize[common.screen])
pygame.display.set_caption("The Snexplorer")
clock = pygame.time.Clock()
block = pygame.image.load("data/newcubes.png")
block = block.convert_alpha() # no fucking way
blkls = [ pygame.transform.scale(block,(119/(60)*i*20,91/60*i*20)) for i in range(3,7)] # better cluster of blocks 120 x 90

snb = pygame.sprite.Group()
player = Snake()
snb.add(player.head)
snb.add(player.tail)
game = game.Game(player,snb)

with open("data/map","r") as f:
    world = []
    rfile = csv.reader(f,delimiter="-")
    for i in rfile:
        world.append(i)

def mapre(cmap,valx,valy): # work on this and inf # work on this and inf # work on this and inf # work on this and inf
    valx *= 2
    valy *= 2
#    valy -= 1
    midx = common.displaymid[common.screen][0]
    midy = common.displaymid[common.screen][1]
    for y,row in enumerate(world):
        for x, col in enumerate(row):
            if col == "1":
                common.vwin.blit(blkls[common.screen],(midx+valx*(x-1)-y*valx,midy-(len(cmap)-y)*valy+x*valy))

while True:
    common.vwin.fill((123,69,30))
    common.time2 = time.time()
    common.dt = 60 * (common.time2 - common.time1)
    common.time1 = time.time()
    
    fps = common.dt**-1*60
    fps = "%.2f" % fps
    mapre(world,common.valx,common.valy) # map being drawn
    game.selector()
    window.blit(common.vwin,(0,0)) # final disp
    window.blit(fontt.render(fps,True,(0,0,0)),(0,0))
    pygame.display.update()
    clock.tick(60)
