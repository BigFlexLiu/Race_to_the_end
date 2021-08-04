"""
    Jan 4, 2018
    encountered some problem
    try to used this to find the solution
    Created by Shenjoe
"""

import pygame
import time

pygame.init()

screen_height = 400
screen_width = 400

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption('Testing')

pygame.draw.rect(screen, (255, 0, 0), [100, 100, 200, 200])
pygame.draw.ellipse(screen, (0, 0, 255), [100, 100, 200, 200])
pygame.draw.circle(screen, (0, 255, 0), (200, 200), 50)
pygame.draw.line(screen, (255, 255, 0), (100, 100), (0, 300))
pygame.draw.arc(screen, (255, 0, 255), (100, 0, 200, 400), 0, 12.6, 5)
pygame.draw.lines(screen, (0, 255, 255), True, ((0, 0), (0, 100), (300, 100), 300, 0))
rect1 = pygame.draw.aaline(screen, (255, 255, 255), (50, 50), (350, 350))
rect2 = pygame.draw.aalines(screen, (255, 255, 255), 1, ((350, 250), (0, 40), (400, 200)))
pygame.display.update()

car_img = pygame.image.load("racecar1.png")
screen.blit(car_img, (0, 0))
pygame.display.update()

px_ary = pygame.PixelArray(screen)
px_ary[350, 100] = (255, 255, 255)
pygame.display.update()


def change_cursor(cursor_type):
    cursor, mask = pygame.cursors.compile(cursor_type)
    size = len(cursor_type[0]), len(cursor_type)
    hot_spot = (0, 0)

    pygame.mouse.set_cursor(size, hot_spot, cursor, mask)


def text_object(text, font):
    font.set_underline(1)
    text_surface = font.render(text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()


def display_text(text, font, size):
    text_font = pygame.font.Font(font, size)
    text_surf, text_rect = text_object(text, text_font)
    text_rect.center = (screen_width/2, screen_height/2)
    screen.blit(text_surf, text_rect)

    pygame.display.update()


font = pygame.font.match_font("Times New Roman")

my_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'greeting': "hello"})


def display_all():
    crashed = False
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    volume = pygame.mixer.music.get_volume()

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    display_text("Hello World!", font, 20)
                if event.key == pygame.K_q:
                    crashed = True
                if event.key == pygame.K_i:
                    print(pygame.display.Info())
                if event.key == pygame.K_f:
                    pygame.mixer.music.fadeout(4000)
                if event.key == pygame.K_KP_PLUS and volume < 1:
                    volume += 0.05
                    pygame.mixer.music.set_volume(volume)
                    print("volume increase to{:f}".format(volume))
                if event.key == pygame.K_MINUS and volume > 0:
                    volume -= 0.05
                    pygame.mixer.music.set_volume(volume)
                    print("volume decrease to {:f}".format(volume))

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                if 0 < mousepos[0] < screen_width / 2 and 0 < mousepos[1] < screen_height / 2:
                    print('yep')

            if event.type == pygame.KEYUP:
                pygame.event.post(my_event)
            print(pygame.event.event_name(event.type))


display_all()

pygame.quit()

quit()


