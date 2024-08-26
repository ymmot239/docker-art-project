import pygame
import os, sys

from pygame import Color

pygame.init()
os.chdir("art-project-main")
#pygame.mixer.init()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/marlboro.ttf", size)

def game_screen(screen):


    while 1:
        screen.fill(Color("#222222"))

        GAME_TEXT = get_font(45).render("This is the GAME screen.", True, "White")
        GAME_RECT = GAME_TEXT.get_rect(center=(640, 50))
        screen.blit(GAME_TEXT, GAME_RECT)

        event = pygame.event.wait()
        cursor = pygame.mouse.get_pos()
        
        holder = pygame.Surface((300,300))
        holder.set_colorkey((0,0,0))
        pygame.draw.polygon(holder, (255,255,255), 
                           ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        holder = pygame.transform.flip(
                     pygame.transform.scale(holder, (80,70)),
                 True,False)
        holder_rect = holder.get_rect(topleft=(10,10))
        screen.blit(holder, holder_rect)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if holder_rect.collidepoint(cursor):
                pygame.mixer.music.stop()
                return
        pygame.display.update()


if __name__ == "__main__":
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Game")

    game_screen(SCREEN)