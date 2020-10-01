import pygame
# import time
# import random


colors = [
    (255, 255, 255),  # Branco
    (0, 0, 0),  # Preto
    (105, 105, 105),  # Cinza
    (139, 0, 0),  # Vermelho Escuro
    (255, 40, 0),  # Vermelho
    (0, 0, 255),  # Azul
    (0, 0, 139),  # Azul Escuro

    (0, 255, 0),  # Verde
    (255, 140, 0),  # Laranja Escuro
    (255, 69, 0),  # Laranja Avermelhado
    (255, 215, 0),  # Ouro
    (240, 230, 140),  # Amarelo Khaki
    (255, 165, 0)  # Laranja
]


class Game:
    def __init__(self, resolution, display, running, screens):
        self.resolution = resolution
        self.display = display
        self.running = running
        self.screens = screens

    def initialPage(self):
        icon = pygame.image.load('./assets/media/icon.png')
        self.display.blit(
            icon, (int(self.resolution[0]/2 - icon.get_width()/2), 0)
        )

        titleFont = pygame.font.Font('./assets/fonts/Roboto-Bold.ttf', 40)
        title = titleFont.render('NetPath', True, colors[1])
        titleArea = title.get_rect()
        titleArea.center = (
            int(self.resolution[0]/2),
            int(title.get_height()/2) + icon.get_height()
        )
        self.display.blit(title, titleArea)

        buttonsTextFont = pygame.font.Font(
            './assets/fonts/Roboto-Bold.ttf', 20
        )
        quitButtonText = buttonsTextFont.render('SAIR', True, colors[0])
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
                self.display, colors[4],
                (
                    quitStart_X, quitStart_Y,
                    quitButtonText_W + 40, quitButtonText_H + 20
                )
            )

        self.display.blit(quitButtonText, (quitStart_X + 20, quitStart_Y + 10))

        subtitleFont = pygame.font.Font('./assets/fonts/Roboto-Bold.ttf', 20)
        subtitle = subtitleFont.render(
            'Um pacote de dados está sendo enviado para um servidor.',
            True, colors[2]
        )
        subtitleArea = subtitle.get_rect()
        subtitleStart_Y = icon.get_height() + title.get_height() + 30
        subtitleArea.center = (
            int(self.resolution[0]/2),
            int(subtitle.get_height()/2) + subtitleStart_Y
        )
        self.display.blit(subtitle, subtitleArea)
        subtitle_1 = subtitleFont.render(
            'Ajude-o a percorrer o menor caminho.',
            True, colors[2]
        )
        subtitleArea_1 = subtitle_1.get_rect()
        subtitleStart_Y_1 = subtitleStart_Y + subtitle.get_height() + 10
        subtitleArea_1.center = (
            int(self.resolution[0]/2),
            int(subtitle_1.get_height()/2) + subtitleStart_Y_1
        )
        self.display.blit(subtitle_1, subtitleArea_1)

        startButtonText = buttonsTextFont.render(
            'INICIAR JOGO', True, colors[0]
        )
        sButtonText_W = startButtonText.get_width()
        sButtonText_H = startButtonText.get_height()

        sButtonStart_X = int(
            self.resolution[0]/2 - sButtonText_W/2 - 20
        )
        sButtonStart_Y = (
            subtitleStart_Y_1 + 65
        )
        if (
            sButtonStart_X <= mouse[0] <= sButtonStart_X + sButtonText_W + 40
            and
            sButtonStart_Y <= mouse[1] <= sButtonStart_Y + sButtonText_H + 20
        ):
            pygame.draw.rect(
                self.display, colors[6],
                (
                    sButtonStart_X, sButtonStart_Y,
                    sButtonText_W + 40, sButtonText_H + 20
                )
            )
        else:
            pygame.draw.rect(
                self.display, colors[5],
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
                    self.screens['questionPage'] = 1
                    self.screens['answerPage'] = 0


def main():
    pygame.init()

    resolution = (800, 600)

    pygame.display.set_caption("NetPath")

    icon = pygame.image.load('./assets/media/icon.png')
    pygame.display.set_icon(icon)

    display = pygame.display.set_mode(resolution)

    screens = {
        'initialPage': 1, 'questionPage': 0, 'answerPage': 0
    }

    newGame = Game(resolution, display, True, screens)

    while newGame.running:
        if newGame.screens['initialPage']:
            display.fill(colors[0])
            newGame.initialPage()
        elif newGame.screens['questionPage']:
            display.fill(colors[1])
        elif newGame.screens['answerPage']:
            print("answerPage")

        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
    quit()
