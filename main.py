import pygame
# import time
# import random


colors = [
    (0, 0, 255)  # Azul
]


def main():
    pygame.init()

    pygame.display.set_caption("undefined")  #

    # icon = pygame.image.load('./assets/media/icon.png')
    # pygame.display.set_icon(icon)

    display = pygame.display.set_mode((800, 600))

    running = True
    while running:
        display.fill(colors[0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


if __name__ == "__main__":
    main()
    quit()
