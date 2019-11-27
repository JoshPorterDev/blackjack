import pygame, sys
from deck import Deck



d = Deck()
d.shuffleDeck()
test_card = d.drawCard()
card_img_id = test_card.test()


pygame.init()

width, height = 500, 500
green = (0, 255, 0)
black = (0, 0, 0)
title = "Blackjack"
icon = pygame.image.load('poker-hand.png')
card = pygame.image.load(f'Medium/{card_img_id}.png')

font = pygame.font.SysFont("Times New Roman", 30)
text = font.render("Black Jack", True, black)

card_text = font.render(f"{card_img_id}", True, black)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)
pygame.display.set_icon(icon)

def cardd(x, y):
    screen.blit(card, (x,y))

x = (width * 0.45)
y = (height * 0.8)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.fill(green)
    cardd(x, y)
    screen.blit(text, (width/2 - text.get_rect().width/2, height/2 - 100))
    screen.blit(card_text, (width/2 - text.get_rect().width/2, height/2))
    pygame.display.flip()
