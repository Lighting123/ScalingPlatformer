import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 400))
clock = pygame.time.Clock()
running = True

# characters
player = pygame.image.load('assets/Characters/tile_0000.png')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    screen.blit(pygame.transform.scale_by(player, 3), (0, 0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
