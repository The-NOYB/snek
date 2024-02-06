import pygame, time

def changewin(window,vwin,screen,ratio):
    screen +=1
    if screen==4: screen = 0
    window = pygame.display.set_mode(displaysize[screen])
    vwin = pygame.Surface((displaysize[screen]))
    ratio = displayunit[screen]/60 
    return vwin,screen,ratio

time1 = time.time()
time2 = 0
dt = 0
displaysize = ((960,540),(1280,720),(1600,900),(1920,1080))
displayunit = [ x[0]//16 for x in displaysize] 
displaymid = [ [displaysize[i][0]//2,displaysize[i][1]//2] for i in range(4)] 
screen = 0
vwin = pygame.Surface(displaysize[screen])
ratio = 1
valx = 30
valy = 16


