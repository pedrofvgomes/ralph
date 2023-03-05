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
        self.x = 0
        self.y = 0
    def left(self):
        if self.x > 0 : self.x -= 1
    def right(self):
        if self.x < 4 : self.x += 1
    def up(self):
        if self.y < 2 : self.y += 1
    def down(self):
        if self.y > 0 : self.y -= 1
    def draw(self, screen):
        # x values
        if self.x == 0:
            drawx = 170
        if self.x == 1:
            drawx = 237
        if self.x == 2:
            drawx = 309
        if self.x == 3:
            drawx = 382
        if self.x == 4:
            drawx = 449

        # y values (a slight difference when he's on the doorway or balcony)

        if self.y == 0:
            drawy = 384
            if self.x == 2:
                drawy = 400
        if self.y == 1:
            drawy = 263
            if self.x == 2:
                drawy = 271
        if self.y == 2:
            drawy = 141


        screen.blit(pygame.image.load('images/felix.png'), (drawx, drawy))

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