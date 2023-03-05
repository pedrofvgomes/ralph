import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((680,480))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
        background = pygame.image.load('images/background.jpg')
        screen.blit(background,(0,0))
        pygame.display.flip()

main()