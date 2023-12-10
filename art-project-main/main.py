import time

import pygame, sys
from button import Button
from music_player import music_player
from current_chat import chat

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/marlboro.ttf", size)

def Ai():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the AI screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    return

        pygame.display.update()
    
def music():
    music_player(SCREEN)
    '''
    while True:
        MUSIC_MOUSE_POS = pygame.mouse.get_pos()
	
        SCREEN.fill("white")

        MUSIC_TEXT = get_font(45).render("This is the MUSIC screen.", True, "Black")
        MUSIC_RECT = MUSIC_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(MUSIC_TEXT, MUSIC_RECT)

        MUSIC_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        MUSIC_BACK.changeColor(MUSIC_MOUSE_POS)
        MUSIC_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MUSIC_BACK.checkForInput(MUSIC_MOUSE_POS):
                    return

        pygame.display.update()
    '''

def movie():
    while True:
        MOVIE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        MOVIE_TEXT = get_font(45).render("This is the Movie screen.", True, "White")
        MOVIE_RECT = MOVIE_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(MOVIE_TEXT, MOVIE_RECT)

        MOVIE_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        MOVIE_BACK.changeColor(MOVIE_MOUSE_POS)
        MOVIE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MOVIE_BACK.checkForInput(MOVIE_MOUSE_POS):
                    return

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Welcome to ART", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        AI_BUTTON = Button(image=pygame.image.load("assets/Short Rect.png"), pos=(350, 400),
                            text_input="AI", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MUSIC_BUTTON = Button(image=pygame.image.load("assets/Short Rect.png"), pos=(900, 400),
                            text_input="MUSIC", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        MOVIE_BUTTON = Button(image=pygame.image.load("assets/Short Rect.png"), pos=(350, 600),
                            text_input="MOVIES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Short Rect.png"), pos=(900, 600),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [AI_BUTTON, MUSIC_BUTTON, MOVIE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AI_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Ai()
                if MUSIC_BUTTON.checkForInput(MENU_MOUSE_POS):
                    music()
                if MOVIE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    movie()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def draw():
    while True:
        pos = pygame.mouse.get_pos()
        print(pos)
        time.sleep(100)


main_menu()
#draw()