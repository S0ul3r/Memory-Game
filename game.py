import pygame, sys, random, time
from pygame.locals import*
from local import*



class Field:
    def __init__(self, color, shape, xcord, ycord, size):
        self.revealed = False
        self.solved = False
        self.color = color
        self.shape = shape
        self.rect  = pygame.Rect(xcord, ycord, size, size)
    
    def isOnTop(self, x, y):
        if( x > self.rect.left and x < self.rect.right and 
        y > self.rect.top and y < self.rect.bottom):
            return True
        else:
            return False



class Game:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
        pygame.display.set_caption('Memory game')
        self.win.fill(WHITE)
        self.tablica = self.convertFields()
        self.tempRevealed = []
        self.tries = 0
        self.revealed = 0
        self.ft = pygame.font.Font('./frog.ttf', 32)
        self.surfFont = self.ft.render('0', True, BLACK, WHITE)




    def handleEvents(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                x, y = event.pos
                self.revealField(x, y)
    
    def update(self):
        return None
    
    def draw(self):
        for i in range(len(self.tablica)):
            for j in range(len(self.tablica[i])):
                self.drawField(self.tablica[i][j])
        self.drawFont()
        pygame.display.update()
    
    def drawFont(self):
        self.surfFont = self.ft.render(str(self.tries), True, BLACK, WHITE)
        surfRect = self.surfFont.get_rect()
        surfRect.left = 5
        surfRect.top = 5
        self.win.blit(self.surfFont, surfRect)

    def play(self):
        self.start()
        while True:
            self.handleEvents()
            self.update()
            self.draw()
    
    def createFields(self):
        pary = []

        for cl in ALLCOLORS:
            for sp in ALLSHAPES:
                pary.append((cl, sp))
        dlugosc = (BOARDHEIGHT * BOARDWIDTH) // 2 
        random.shuffle(pary)
        pary = pary[:dlugosc] * 2
        random.shuffle(pary)
        tablica_par = []

        for x in range(BOARDWIDTH):
            kolumna = []
            for y in range(BOARDHEIGHT):
                kolumna.append(pary[0])
                del pary[0]
            tablica_par.append(kolumna)
        return tablica_par
    
    def convertFields(self):
        tab = self.createFields()
        pom = []
        for x in range(len(tab)):
            c = []
            for y in range(len(tab[x])):
                i = Field(tab[x][y][0], tab[x][y][1], XMARGIN + x*(BOXSIZE+GAPSIZE),
                YMARGIN + y*(BOXSIZE + GAPSIZE), BOXSIZE)
                c.append(i)
            pom.append(c)
        return pom
        

    def drawField(self,field):
        if field.revealed == True or field.solved == True:
            half = BOXSIZE // 2
            quart = BOXSIZE // 4

            pygame.draw.rect(self.win, WHITE, field.rect)
            if field.shape == DONUT:
                pygame.draw.circle(self.win, field.color, (field.rect.left + half,field.rect.top + half), half - 5)
                pygame.draw.circle(self.win, WHITE, (field.rect.left + half,field.rect.top + half), quart - 5)
            elif field.shape == SQUARE:
                pygame.draw.circle(self.win, field.color, (field.rect.left + half,field.rect.top + half), half - 5)
            elif field.shape == DIAMOND :
                pygame.draw.polygon(self.win, field.color,  ((field.rect.left + half, field.rect.top), (field.rect.left
                + BOXSIZE - 1, field.rect.top + half), (field.rect.left + half, field.rect.top + BOXSIZE - 1),
                 (field.rect.left, field.rect.top +half)))
            elif field.shape == OVAL:
                pygame.draw.ellipse(self.win, field.color,  (field.rect.left, field.rect.top + quart,
                BOXSIZE, half))

            elif field.shape == LINES:
                for i in range(0, BOXSIZE, 4):
                    pygame.draw.line(self.win, field.color, (field.rect.left, field.rect.top + i), (field.rect.left +
                    i, field.rect.top))

                    pygame.draw.line(self.win, field.color, (field.rect.left + i, field.rect.top + BOXSIZE- 1),
                     (field.rect.left + BOXSIZE - 1, field.rect.top + i))
        else:
            pygame.draw.rect(self.win, (100, 100, 150), field.rect) 
        
        
    def revealField(self, x, y):
        for i in range(len(self.tablica)):
            for j in range(len(self.tablica[i])):
                if(self.tablica[i][j].revealed == False and self.tablica[i][j].isOnTop(x, y)):
                    self.tempRevealed.append(self.tablica[i][j])
                    self.tries += 1
                    print(len(self.tempRevealed))
                    if len(self.tempRevealed) <= 1:
                        self.tablica[i][j].revealed = True
                    elif len(self.tempRevealed) == 2:
                        if (self.tempRevealed[0].shape == self.tempRevealed[1].shape and
                        self.tempRevealed[0].color == self.tempRevealed[1].color):

                            self.tempRevealed[0].revealed = True
                            self.tempRevealed[1].revealed = True
                            self.tempRevealed[0].solved = True
                            self.tempRevealed[1].solved = True
                            self.revealed += 2
                        else:
                            self.tempRevealed[0].revealed = True
                            self.tempRevealed[1].revealed = True
                            self.draw()
                            time.sleep(0.5)
                            self.tempRevealed[0].revealed = False
                            self.tempRevealed[1].revealed = False
                            self.tempRevealed[0].solved = False
                            self.tempRevealed[1].solved = False
                        
                        self.tempRevealed.pop()
                        self.tempRevealed.pop()





    def revealXY(self, x, y):
        assert x > BOARDWIDTH or x < 0 or y > BOARDHEIGHT or y < 0, 'Nie ma takiego pola'
        self.tablica[x][y].revealed = True

    def revealAll(self):
        for i in self.tablica:
            for j in i:
                j.revealed = True

    def hideAll(self):
        for i in self.tablica:
            for j in i:
                j.revealed = False
    
    def start(self):
        self.draw()
        time.sleep(0.25)
        self.revealAll()
        self.draw()
        time.sleep(3)
        self.hideAll()
        self.draw()
    
