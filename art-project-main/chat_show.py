from current_chat import chat
import pygame, sys
from pygame import Color

pygame.init()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/marlboro.ttf", size)

def chat_screen(screen):
    pygame.display.set_caption("Chat")

    holder = pygame.Surface((300,300))
    holder.set_colorkey((0,0,0))
    pygame.draw.polygon(holder, (255,255,255), 
                       ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
    holder = pygame.transform.flip(
                 pygame.transform.scale(holder, (80,70)),
             True,False)
    holder_rect = holder.get_rect(topleft=(10,10))

    CHAT_TEXT = get_font(45).render("This is the CHAT screen.", True, "White")
    CHAT_RECT = CHAT_TEXT.get_rect(center=(640, 50))

    while True:
        screen.fill(Color("#222222"))

        screen.blit(holder, holder_rect)
        screen.blit(CHAT_TEXT, CHAT_RECT)

        event = pygame.event.wait()
        cursor = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if holder_rect.collidepoint(cursor):
                return

        pygame.display.update()

if __name__ == '__main__':
    pass