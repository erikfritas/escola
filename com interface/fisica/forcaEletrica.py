# não está pronto, só comecei o projeto
import pygame as pyg
FPS = 60
clock = pyg.time.Clock()
from pygame.locals import *

pyg.init()

WINDOW_SIZE = [800, 600]
screen = pyg.display.set_mode(WINDOW_SIZE, RESIZABLE)


class Game:
    def __init__(self):
        COLOR_INACTIVE = pyg.Color('lightskyblue3')
        COLOR_ACTIVE = pyg.Color('dodgerblue2')
        fonte = pyg.font.SysFont('consolas', 50)
        digitado = ['']
        size_max = 200
        class InputBox:
            def __init__(self, x, y, w, h, text=''):
                self.rect = pyg.Rect(x, y, w, h)
                self.color = COLOR_ACTIVE
                self.text = text
                self.txt_surface = fonte.render(text, True, self.color)
                self.ativo = True

            def handle_event(self, event):
                global digitado
                if event.type == pyg.MOUSEBUTTONDOWN:
                    self.ativo = True
                    self.color = COLOR_ACTIVE if self.ativo else COLOR_INACTIVE
                if event.type == KEYDOWN:
                    if self.ativo:
                        if event.key == K_RETURN:
                            digitado[0] = self.text
                            self.text = ''
                        elif event.key == K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
                        self.txt_surface = FONT.render(self.text, True, self.color)

            def update(self):
                width = max(size_max, self.txt_surface.get_width() + 10)
                self.rect.w = width

            def draw(self, scr):
                scr.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
                pyg.draw.rect(screen, self.color, self.rect, 2)

        def update():
            global done
            clock.tick(FPS)
            for e in pyg.event.get():
                if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
                    pyg.quit()

        def render():
            screen.fill((0, 0, 10))

        while True:
            try:
                update()
                render()
                pyg.display.update()
            except pyg.error:
                break


if __name__ == '__main__':
    Game()
    exit()
