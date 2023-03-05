import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((680,480))
    felix = Felix()
    running = True
    clouds = [Cloud(40), Cloud(140), Cloud(240)]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a] : felix.left()
                if event.key in [pygame.K_RIGHT, pygame.K_d]: felix.right()
                if event.key in [pygame.K_UP, pygame.K_w]: felix.up()
                if event.key in [pygame.K_DOWN, pygame.K_s]: felix.down()
        screen.fill((0,0,0))
        for cloud in clouds:
            if cloud.visible: cloud.draw(screen)
            else:
                n = random.randrange(0,500)
                if n==0: cloud.spawn()

        screen.blit(pygame.image.load('images/background.png'),(0,0))
        felix.draw(screen)
        pygame.display.flip()

class Felix:
    def __init__(self):
        self.x = 170
        self.y = 384
        self.status = 'standing'

    def left(self):
        # start moving
        if self.status == 'standing' and self.x >= 170:
            self.status = 'jumping left'

    def right(self):
        if self.status == 'standing' and self.x <= 409:
            self.status = 'jumping right'

    def up(self):
        if self.status == 'standing' and self.y < 409:
            self.status = 'jumping up'

    def down(self):
        if self.status == 'standing' and self.y >= 141:
            self.status = 'jumping down'

    def draw(self, screen):
        if self.status == 'jumping left':
            self.x-=1
            # jumps 4-3 and 1-0 1st and 2nd floor
            if (self.x > 170 and self.x < 203.5) or (self.x > 382 and self.x < 415.5) and self.y > 200:
                self.y+=0.5
            if (self.x > 203.5 and self.x < 237) or (self.x > 415.5 and self.x < 449) and self.y > 200:
                self.y-=0.5
            
            # jumps 3-2 and 2-1 1st floor
            if self.x in [245,249,253,257,261,265,269,273,277,281,285,289,293,297,301,305] and self.y > 350:
                self.y-=1
            if self.x in [313,317,321,325,329,333,337,341,345,349,353,357,361,365,369,373] and self.y > 350:
                self.y+=1

            # jumps 3-2 and 2-1 1st floor
            if self.x in [245,249,253,257,261,265,269,273,277,281,285,289,293,297,301,305] and self.y > 200 and self.y < 300:
                self.y-=0.5
            if self.x in [313,317,321,325,329,333,337,341,345,349,353,357,361,365,369,373] and self.y > 200 and self.y < 300:
                self.y+=0.5

            # every 3rd floor jump
            if (self.x > 170 and self.x < 203.5) or (self.x > 237 and self.x < 273) or (self.x > 309 and self.x < 345) or (self.x > 382 and self.x < 415.5):
                if self.y < 200: self.y+=0.5
            if (self.x > 203.5 and self.x < 237) or (self.x > 273 and self.x < 309) or (self.x > 345 and self.x < 382) or (self.x > 415.5 and self.x < 449):
                if self.y < 200: self.y-=0.5

        if self.status == 'jumping right':
            self.x+=1
            # jumps 0-1 and 3-4 1st and 2nd floor
            if (self.x > 170 and self.x < 203.5) or (self.x > 382 and self.x < 415.5) and self.y > 200:
                self.y-=0.5
            if (self.x > 203.5 and self.x < 237) or (self.x > 415.5 and self.x < 449) and self.y > 200:
                self.y+=0.5

            # jumps 1-2 and 2-3 1st floor
            if self.x in [245,249,253,257,261,265,269,273,277,281,285,289,293,297,301,305] and self.y > 350:
                self.y+=1
            if self.x in [313,317,321,325,329,333,337,341,345,349,353,357,361,365,369,373] and self.y > 350:
                self.y-=1

            # jumps 3-2 and 2-1 1st floor
            if self.x in [245,249,253,257,261,265,269,273,277,281,285,289,293,297,301,305] and self.y > 200 and self.y < 300:
                self.y+=0.5
            if self.x in [313,317,321,325,329,333,337,341,345,349,353,357,361,365,369,373] and self.y > 200 and self.y < 300:
                self.y-=0.5
            
            # every 3rd floor jump
            if (self.x > 170 and self.x < 203.5) or (self.x > 237 and self.x < 273) or (self.x > 309 and self.x < 345) or (self.x > 382 and self.x < 415.5):
                if self.y < 200: self.y-=0.5
            if (self.x > 203.5 and self.x < 237) or (self.x > 273 and self.x < 309) or (self.x > 345 and self.x < 382) or (self.x > 415.5 and self.x < 449):
                if self.y < 200: self.y+=0.5
        
        if self.status == 'jumping up':
            self.y -= 1
        
        if self.status == 'jumping down':
            self.y += 1

        # standing positions
        if (self.x, self.y) in [(170,384), (170,263), (170,141), (237,384), (237,263), (237,141), (309,400), (309,271), (309,141), (382,384), (382,263), (382,141), (449,384), (449,263), (449,141)]:
            self.status = 'standing'

        if self.status == 'standing':
            icon = pygame.image.load('images/felix_standing.png')
        if self.status == 'jumping left':
            icon = pygame.image.load('images/felix_jumping_left.png')
        if self.status == 'jumping right':
            icon = pygame.image.load('images/felix_jumping_right.png')
        if self.status in ['jumping down', 'jumping up']:
            icon = pygame.image.load('images/felix_jumping_right.png')
    
        screen.blit(icon, (self.x, self.y))

class Cloud:
    def __init__(self, y):
        self.visible = False
        self.x = 0       
        self.y = y
        self.velocity = 0
    def spawn(self):
        n = random.randrange(0,2)
        self.visible = True
        if n==0: 
            self.x = -200
            self.velocity = 0.5
        else: 
            self.x = 850
            self.velocity = -0.5
        self.velocity*= random.randrange(1,5)

    def draw(self, screen):
        screen.blit(pygame.image.load('images/cloud.png'), (self.x, self.y))
        self.x = self.x + self.velocity
        if self.x > 850 or self.x < -200:
            self.velocity = 0
            self.visible = False


main()