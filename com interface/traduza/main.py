import pygame as pyg
from pygame.locals import *
from random import randint, choices

FPS = 60
clock = pyg.time.Clock()

pyg.init()
words = []
palavras = []
COLOR_INACTIVE = pyg.Color('lightskyblue3')
COLOR_ACTIVE = pyg.Color('dodgerblue2')
FONT = pyg.font.Font(None, 50)
digitado = ['']
size_max = 200

WINDOW_SIZE = [800, 600]
screen = pyg.display.set_mode(WINDOW_SIZE, RESIZABLE)
caps = ['digita um negocio em ingles ai meo', 'cha de ser besta', 'irra i am a caubói']
caption = choices(caps, weights=[2, 4, 6])
pyg.display.set_caption(caption[0])

pontos = 0
with open('data/english.txt') as en, open('data/portugues.txt') as pt, open('data/pontos.txt') as pnt:
    pontos += int(pnt.readlines()[0])
    for ew in en:
        words.append(ew.replace('\n', '').lower())
    for pw in pt:
        palavras.append(pw.replace('\n', '').lower())

cont = randint(0, len(palavras))
ac = 0
rc = False
mcolor = (10, 100, 100)
resposta = False


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pyg.Rect(x, y, w, h)
        self.color = COLOR_ACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.ativo = True

    def handle_event(self, event):
        global digitado
        if event.type == pyg.MOUSEBUTTONDOWN:
            self.ativo = True
            self.color = COLOR_ACTIVE if self.ativo else COLOR_INACTIVE
        if event.type == KEYDOWN:
            if self.ativo:
                if event.key == pyg.K_RETURN:
                    digitado[0] = self.text
                    self.text = ''
                elif event.key == pyg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(size_max, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, scr):
        scr.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pyg.draw.rect(screen, self.color, self.rect, 2)


def update():
    global resposta, pontos
    clock.tick(FPS)

    for e in pyg.event.get():
        if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
            pyg.quit()
            exit()
        for box in input_boxes:
            box.handle_event(e)
        if e.type == KEYDOWN:
            if e.key == K_LCTRL:
                resposta = True
                if pontos >= 1:
                    pontos -= 1

    for box in input_boxes:
        box.update()


txtbox = InputBox(300, 280, 200, 50)
input_boxes = [txtbox]


def render():
    global cont, ac, mcolor, resposta, pontos, rc
    screen.fill((0, 0, 10))

    if digitado[0].lower() == palavras[cont].lower():
        cont = randint(0, len(palavras))
        ac = 100
        resposta = False
        pontos += 1
        with open('data/pontos.txt', 'w') as pnts:
            pnts.writelines(str(pontos))

    if 0 < ac <= 100:
        pyg.draw.rect(screen, (10, 100, 10), (10, 300, int(ac/2), int(ac/2)))
        ac -= 1

    ajudinha = pyg.draw.rect(screen, mcolor, (300, 350, 60, 30))
    if ajudinha.collidepoint(pyg.mouse.get_pos()):
        mcolor = (100, 100, 10)
        if pyg.mouse.get_pressed(3)[0]:
            resposta = True
            rc = True
        elif pontos >= 1 and rc:
            pontos -= 1
            rc = False
    else:
        mcolor = (10, 100, 100)

    screen.blit(FONT.render(words[cont], True, (200, 200, 200)), (300, 200))
    if resposta:
        screen.blit(FONT.render(f'Resposta: {words[cont]} = {palavras[cont]}', True, (200, 200, 200)), (100, 450))
    screen.blit(FONT.render(f'Pontuação: {pontos}', True, (200, 200, 200)), (5, 5))

    for box in input_boxes:
        box.draw(screen)


while True:
    update()
    render()
    pyg.display.update()
