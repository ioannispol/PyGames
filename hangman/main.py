"""
Python Hangman Game
from tutorial:
https://www.youtube.com/watch?v=UEO1B_llDnc&list=PLzMcBGfZo4-ndZlN21DasvpfKwIc1rI6w
"""

import pygame
import math

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500  # Make variable names all capitals
# Create the dimenstions of the pygame script
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH  - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)

# game variables
hangman_status = 0

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    # draw buttons
    for letter in letters:
        x, y, ltr, vissible = letter
        if vissible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_width()/2))

    # draw the correct image and display it on the window at the coordinates (x, y)
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()  # top lefe t corner is (0, 0)
            for letter in letters:
                x, y, ltr, vissible = letter
                if vissible:
                    # use Pythagorian theorem to determine the distance between the mouse and the button
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False


pygame.quit()

