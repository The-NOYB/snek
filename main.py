import pygame,math,sys,time
import common
from game import Game

pygame.init()
fontt = pygame.font.Font(None,size=48)
window = pygame.display.set_mode(common.displaysize)
pygame.display.set_caption("The Snexplorer")
clock = pygame.time.Clock()


game = Game()


while True:
    common.vwin.fill((123,69,30))
    common.time2 = time.time()

    common.dt = 60 * (common.time2 - common.time1)
    common.time1 = time.time()
    
    fps = common.dt**-1*60
    fps = "%.2f" % fps
    game.selector()
    window.blit(common.vwin,(0,0)) # final disp
    window.blit(fontt.render(fps,True,(0,0,0)),(0,0))
    pygame.display.update()
    clock.tick(60)
