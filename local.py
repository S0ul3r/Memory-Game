FPS = 60
WINDOWWIDTH = 800
WINDOWHEIGHT = 480
BOXSIZE = 50
GAPSIZE = 12
BOARDWIDTH = 5
BOARDHEIGHT = 4
assert (BOARDHEIGHT * BOARDWIDTH) % 2 == 0, 'Musi byc parzysta liczba pol'

XMARGIN = (WINDOWWIDTH - (BOXSIZE + GAPSIZE) * BOARDWIDTH + GAPSIZE)//2
YMARGIN = (WINDOWHEIGHT - (BOXSIZE + GAPSIZE) * BOARDHEIGHT + GAPSIZE)//2


GRAY = (128, 128, 128)
NAVY = (0, 0, 128)
TEAL = (0, 128, 128)
PURPLE = (128, 0, 128)
GREEN = (0, 128, 0)
OLIVE = (128, 128, 0)
MAROON = (128, 0, 0)
MAGNETA = (255, 0, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255,255)
BLACK = (0, 0, 0)

BGCOLOR = NAVY
LIGHTBGCOLOR = GRAY
BOXCOLOR = BLUE
HIGHLIGHTCOLOR = PURPLE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (GRAY, NAVY, TEAL, PURPLE, GREEN, OLIVE, MAROON, MAGNETA, YELLOW, BLUE)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

assert len(ALLCOLORS)* len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, 'Jest za malo kolorow i ksztaltow zeby starczylo na wszystkie pola'
