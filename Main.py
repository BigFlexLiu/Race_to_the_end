"""
    Jan 4, 2018
    The main file for the game, not sure if there'll be more files
    Created by Shenjoe
"""

import pygame
import time
import random
import sys

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (180, 180, 180)

car_width = 73

display_width = 500
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Car race')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar1.png')

sad_music = r"C:\Users\Shenjoe\Music\Random collection\Sad Violin all in 30 seconds.mp3"
game_music = "Initial_D_Deja_Vu.mp3"


def play_music(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)


def objs(obj_x, obj_y, obj_w, obj_h, obj_color):
    pygame.draw.rect(game_display, obj_color, (obj_x, obj_y, obj_w, obj_h))


def car(x, y):
    game_display.blit(carImg, (x, y))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def button_maker(button_height, color_text, color_background, text_info, width_div, height_mult):
    font_type = pygame.font.match_font("Times New Roman")

    font = pygame.font.Font(font_type, button_height)
    text_surf = font.render(text_info, True, color_text, color_background)
    text_rect = text_surf.get_rect()
    text_rect.center = (display_width // width_div, display_height * height_mult)
    game_display.blit(text_surf, text_rect)

    return text_rect


def game_start_menu():
    font_type = pygame.font.match_font('arial')
    font = pygame.font.Font(font_type, 110)
    text_surf = font.render("Car race", True, green)
    text_placement = ((display_width - text_surf.get_width()) // 2, (display_height - text_surf.get_height())//2.5)
    game_display.blit(text_surf, text_placement)

    pygame.display.update()


def start_menu_loop():
    game_display.fill(white)
    rect = button_maker(50, black, blue, "start", 2, 0.75)
    game_start_menu()

    conti_loop = True

    while conti_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if rect[0] < x < rect[0] + rect[2] and rect[1] < y < rect[1] + rect[3]:
                    conti_loop = False


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 85)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = (display_width / 2, (display_height / 2))
    game_display.blit(text_surf, text_rect)

    pygame.display.update()

    time.sleep(2)


def score_display(score):
    font_type = pygame.font.match_font('Times New Roman', 1)
    font = pygame.font.Font(font_type, 30)
    text_surf = font.render(score, True, red)
    text_width = text_surf.get_width() * 1.2
    game_display.blit(text_surf, (display_width - text_width, 20))

    pygame.display.update()


# end of game, displays you crashed on screen
def crashed():
    message_display('You crashed')


# Click yes button returns True, click no button returns false
def game_over_click(yes_rect, no_rect):
    play_music(sad_music)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if yes_rect[1] < y < yes_rect[1] + yes_rect[3]:
                    if yes_rect[0] < x < yes_rect[0] + yes_rect[2]:
                        return True
                    elif no_rect[0] < x < no_rect[0] + no_rect[2]:
                        return False


# Called after crashing
def game_over():
    game_display.fill(white)
    font_type = pygame.font.match_font("Times New Roman", 1, 1)
    font = pygame.font.Font(font_type, 50)
    text_surf = font.render("GAME OVER", 1, black)
    text_rect = text_surf.get_rect()
    text_rect.center = (display_width // 2, display_height * 0.25)
    game_display.blit(text_surf, text_rect)
    text_surf = font.render("Continue?", 1, black)
    text_rect = text_surf.get_rect()
    text_rect.center = (display_width // 2, display_height * 0.4)
    game_display.blit(text_surf, text_rect)
    yes_button = button_maker(50, blue, gray, "Yes", 3, 0.65)
    no_button = button_maker(50, red, gray, "No", 1.5, 0.65)

    pygame.display.update()

    return game_over_click(yes_button, no_button)


def game_loop():

    # x is horizontal position of car and y is the vertical position
    x = display_width * 0.5   # (display_width * 0.45)
    y = display_height * 0.8  # (display_height * 0.8)

    # The amount which car moves horizontally by in each frame
    x_change = 0

    # setting of object which the player will try to dodge
    obj_speed = 10
    obj_width = 100
    obj_height = 100
    speed_incre = 1
    # randomly position obj inside screen
    obj_x = random.randint(0, display_width - obj_width)
    # give time for player to get ready to dodge
    obj_y = -3 * display_height

    # game loop exits when this variable becomes True
    game_exit = False
    score = 0

    start_menu_loop()

    play_music(game_music)

    # allow the events to repeat until user exits the game
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # end game when the x button on top right corner is pressed
            if event.type == pygame.QUIT:
                game_exit = True
                crashed()

            if event.type == pygame.KEYDOWN:
                # let car move left and right when the corresponding arrow key is pressed
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                # end game if 'q' is pressed
                elif event.key == pygame.K_q:
                    game_exit = True
                    crashed()
            # reset the movement of car back to 0 per frame
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0

        # change car position
        x += x_change

        # stops car from moving out of screen
        if 0 > x or x > display_width - 73:
            x -= x_change

        game_display.fill(white)
        car(x, y)

        # generates another object at random place on screen when the current object goes out of screen
        if obj_y > display_height:
            obj_y -= random.randint(display_height, display_height * 1.2)
            obj_x = random.randint(0, display_width - obj_width)
            score += 1
            if score == speed_incre * 10:
                obj_speed += 1
                speed_incre += 1

        # draw the object
        objs(obj_x, obj_y, obj_width, obj_height, black)
        # move the object down the screen
        obj_y += obj_speed

        if obj_x - obj_width < x < obj_x + obj_width and y < obj_height + obj_y:
            game_exit = True
            crashed()

        score_display("score: " + str(score))
        # updates screen with new frame
        pygame.display.update()

        clock.tick(60)

    exit_or_restart = game_over()
    if exit_or_restart is True:
        game_loop()


game_loop()
pygame.quit()
quit()

