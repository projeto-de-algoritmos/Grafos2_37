import pygame
# import time
# import random


colors = [
    (0, 0, 0),  # Preto
    (255, 255, 255),  # Branco
    (255, 40, 0),  # Vermelho
    (139, 0, 0),  # Vermelho Escuro
    (0, 0, 255),  # Azul
    (0, 0, 139),  # Azul Escuro

    (105, 105, 105),  # Cinza
    (0, 255, 0),  # Verde
    (255, 140, 0),  # Laranja Escuro
    (255, 69, 0),  # Laranja Avermelhado
    (255, 215, 0),  # Ouro
    (240, 230, 140),  # Amarelo Khaki
    (255, 165, 0)  # Laranja
]

graph = {
    'A': {'B': 0, 'C': 0},
    'B': {'D': 0, 'F': 0},
    'C': {'D': 0, 'E': 0},
    'D': {'E': 0, 'F': 0},
    'E': {'G': 0},
    'F': {'E': 0, 'H': 0}
}

A: (300, 70) 
B: (450, 140)
C: (150, 140)
D: (300, 210)
E: (150, 280)
F: (450, 350)
G: (200, 420)
H: (400, 730)


class Game:
    def __init__(self, resolution, display, running, screens):
        self.resolution = resolution
        self.display = display
        self.running = running
        self.screens = screens

    def initialPage(self):
        icon = pygame.image.load('./assets/media/icon.png')
        self.display.blit(
            pygame.transform.scale(icon, (200, 177)),
            (int(self.resolution[0]/2 - 100), 40)
        )

        titleFont = pygame.font.Font('./assets/fonts/Roboto-Bold.ttf', 40)
        title = titleFont.render('dPath', True, colors[1])
        titleArea = title.get_rect()
        titleArea.center = (
            int(self.resolution[0]/2),
            int(title.get_height()/2) + 177 + 40 + 40
        )
        self.display.blit(title, titleArea)

        buttonsTextFont = pygame.font.Font(
            './assets/fonts/Roboto-Bold.ttf', 20
        )
        quitButtonText = buttonsTextFont.render('SAIR', True, colors[1])
        quitButtonText_W = quitButtonText.get_width()
        quitButtonText_H = quitButtonText.get_height()

        mouse = pygame.mouse.get_pos()

        quitStart_X = (
            int(self.resolution[0]/2 - quitButtonText_W/2 - 20)
        )
        quitStart_Y = (
            self.resolution[1] - 40 - quitButtonText_H - 20
        )
        if (
            quitStart_X <= mouse[0] <= quitStart_X + quitButtonText_W + 40
            and quitStart_Y <= mouse[1] <= quitStart_Y + quitButtonText_H + 20
        ):
            pygame.draw.rect(
                self.display, colors[3],
                (
                    quitStart_X, quitStart_Y,
                    quitButtonText_W + 40, quitButtonText_H + 20
                )
            )
        else:
            pygame.draw.rect(
                self.display, colors[2],
                (
                    quitStart_X, quitStart_Y,
                    quitButtonText_W + 40, quitButtonText_H + 20
                )
            )

        self.display.blit(quitButtonText, (quitStart_X + 20, quitStart_Y + 10))

        startButtonText = buttonsTextFont.render(
            'ENCONTRAR MENOR CAMINHO', True, colors[1]
        )
        sButtonText_W = startButtonText.get_width()
        sButtonText_H = startButtonText.get_height()

        sButtonStart_X = int(
            self.resolution[0]/2 - sButtonText_W/2 - 20
        )
        sButtonStart_Y = (
            177 + 40 + 40 + title.get_height() + 40
        )
        if (
            sButtonStart_X <= mouse[0] <= sButtonStart_X + sButtonText_W + 40
            and
            sButtonStart_Y <= mouse[1] <= sButtonStart_Y + sButtonText_H + 20
        ):
            pygame.draw.rect(
                self.display, colors[5],
                (
                    sButtonStart_X, sButtonStart_Y,
                    sButtonText_W + 40, sButtonText_H + 20
                )
            )
        else:
            pygame.draw.rect(
                self.display, colors[4],
                (
                    sButtonStart_X, sButtonStart_Y,
                    sButtonText_W + 40, sButtonText_H + 20
                )
            )

        self.display.blit(
            startButtonText, (sButtonStart_X + 20, sButtonStart_Y + 10)
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                quit_H = quitButtonText_H
                quit_W = quitButtonText_W
                if (
                    quitStart_X <= mouse[0] <= quitStart_X + quit_W + 40
                    and quitStart_Y <= mouse[1] <= quitStart_Y + quit_H + 20
                ):
                    self.running = False

                start_W = sButtonText_W
                start_H = sButtonText_H
                if (
                    sButtonStart_X <= mouse[0] <= sButtonStart_X + start_W + 40
                    and
                    sButtonStart_Y <= mouse[1] <= sButtonStart_Y + start_H + 20
                ):
                    self.screens['initialPage'] = 0
                    self.screens['searchPage'] = 1


def main():
    pygame.init()

    resolution = (800, 600)

    pygame.display.set_caption("dPath")

    icon = pygame.image.load('./assets/media/icon.png')
    pygame.display.set_icon(icon)

    display = pygame.display.set_mode(resolution)

    screens = {
        'initialPage': 1, 'searchPage': 0
    }

    newGame = Game(resolution, display, True, screens)

    while newGame.running:
        display.fill(colors[0])

        if newGame.screens['initialPage']:
            newGame.initialPage()
        elif newGame.screens['searchPage']:
            print("SearchPage")

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
