import pygame
import random
import time

pygame.init()

screen_width = 900
screen_height = 700

screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption('Recycle Marathon')

def change_background():
    background=pygame.image.load("bground.png")
    bg=pygame.transform.scale(background,(screen_width, screen_height))
    screen.blit(bg,(0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('bin.png')
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('plastic.png')
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

class recycable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image,(30,30))
        self.rect=self.image.get_rect()

#groups = to put things together under one name
item_list = pygame.sprite.Group() #recycable
plastic_list = pygame.sprite.Group() # non-recycable
allsprites = pygame.sprite.Group()

bin=Bin()
allsprites.add(bin)

#to create list is variable = ["", ""]
images = ["item1.png", "item2.png", "item3.png"]

for i in range(50):
    item=recycable(random.choice(images)) #select random value from list = random.choice(variable)
    item.rect.x=random.randrange(screen_width) #from screen = random.randrange(SW or SH)
    item.rect.y=random.randrange(screen_height)
    item_list.add(item) #to add items from list you do list.add(item)
    allsprites.add(item) #to add item to sprites allocation so you would do allsprites.add(item)

for i in range(20):
    plastic=non_recyclable()
    plastic.rect.x=random.randrange(screen_width)
    plastic.rect.y=random.randrange(screen_height)
    plastic_list.add(plastic)
    allsprites.add(plastic)

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255, 0)

playing = True
score = 0 
# to add a timed system onto the screen
clock = pygame.time.Clock()
start_time = time.time()

myFont = pygame.font.SysFont("Times New Roman", 22)
#sysfont is text in the system and render is to project the text
text = myFont.render("Score =" + str(0), True, BLACK) #str is sting for writing out code in a line added to the text as a number 

#imfinite loop is to add while True
while playing:
    #can be used to control the speed of the game
    clock.tick(60)

    for event in pygame.event.get(): #event is somehting that happens on command during the game
        if event.type == pygame.QUIT:
            playing=False

    timeElapsed=time.time()-start_time # calcualting time taken
    if timeElapsed >=60: #time taken
        if score >=20:
            screen.fill(GREEN)
            text1=myFont.render("Bin loot successful!",True,BLACK)
        else:
            screen.fill(RED)
            text1=myFont.render("Better luck next time!",True,BLACK)
        screen.blit(text1,(250,40))
    else:
        change_background()
        countDown = myFont.render("Time Left:" + str(60 - int(timeElapsed)), True, BLACK)
        screen.blit(countDown, (20,10))

        #to control with mouse-keys up and down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y >0:
                bin.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if bin.rect.y <630:
                bin.rect.y += 5
        #to control with mouse-keys left and right
        if keys[pygame.K_LEFT]:
            if bin.rect.x >0:
                bin.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            if bin.rect.x <850:
                bin.rect.x += 5

        item_hit_list=pygame.sprite.spritecollide(bin, item_list, True)

        for item in item_hit_list:
            score +=1
            text = myFont.render("Score =" + str(score), True, BLACK)

        plastic_hit_list=pygame.sprite.spritecollide(bin, plastic_list, True)

        for plastic in plastic_hit_list:
            score -= 5
            text = myFont.render("Score=" + str(score), True, BLACK)

    screen.blit(text, (20, 50))
    allsprites.draw(screen)
    pygame.display.update()

pygame.quit()





        
            




















































        


