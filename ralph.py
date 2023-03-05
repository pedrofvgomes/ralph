import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
        screen.fill((0,0,0))
        pygame.display.flip()

main()