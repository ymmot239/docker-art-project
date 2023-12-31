from current_chat import chat
import pygame, sys
from pygame import Color
from pathlib import Path

pygame.init()

held_surface = []
held_text = ""


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/marlboro.ttf", size)


def get_log():
    data = Path("text_log.txt").read_text()  
    return str(data)


def write_log(text):
    f = open("text_log.txt","w")
    f.write(text)
    f.close()


def full_text(max_width, text, font, color=pygame.Color('White')):
    global held_text
    global held_surface
    if text == held_text:
        return held_surface
    held_text = text
    surface = pygame.Surface((max_width,3000),pygame.SRCALPHA)
    surface.fill((0,0,0,0))
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    word_surface = font.render("hi", True, color)
    word_width, word_height = word_surface.get_size()
    x, y = 10, word_height + 10

    to_be_continued = font.render("...",0,color)
    
    for linex in range(len(words)-1,0,-1):
        line = words[linex]
        temp = pygame.Surface((max_width, 95),pygame.SRCALPHA)
        temp.fill((0,0,0,0))
        tempy = 10
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = 10  # Reset the x.
                y += word_height  # Start on new row.
                tempy += word_height
            if tempy >= 95:
                surface.blit(to_be_continued, (20,3000-y+100))
                break
            temp.blit(word_surface, (x, tempy))
            x += word_width + space
        surface.blit(temp, (10,3000-y))
        x = 10  # Reset the x.
        y += word_height  # Start on new row.
        if y > 3000:
            break

    return_surface = pygame.Surface((max_width, y+10),pygame.SRCALPHA)
    return_surface.fill((0,0,0,0))
    return_surface.blit(surface,(10,10))
    held_surface = return_surface
    return return_surface


def partial_text(screen, max_width, max_height, text, font, scroll):
    moveLogArea = pygame.Rect(100, 110, max_width, max_height)
    pygame.draw.rect(screen , pygame.Color("gray"), moveLogArea)

    text_surface = full_text(max_width, text, font)
    #screen.blit(text_surface, text_surface.get_rect(topleft=(100,110)))
    
    dy = text_surface.get_height() - max_height
    if dy > 0:
        text_offset = int(dy * (scroll/10)) 
        test_rect = text_surface.get_rect()
        sub_rect = pygame.Rect(0, text_offset, max_width, max_height)
        sub_text_surface = text_surface.subsurface(sub_rect)
        screen.blit(sub_text_surface, moveLogArea)
    else:
        screen.blit(text_surface, moveLogArea)
    

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
    
    scroll = 10
    user_input = ""
    user_log = get_log()
    input_rect = pygame.Rect(100,640, 140, 32) 
    
    while True:
        screen.fill(Color("#222222"))

        screen.blit(holder, holder_rect)
        screen.blit(CHAT_TEXT, CHAT_RECT)

        event = pygame.event.wait()
        cursor = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            write_log(user_log)
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if holder_rect.collidepoint(cursor):
                write_log(user_log)
                return

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1] 

            elif event.key == pygame.K_RETURN:
                user_log += "\n> " + user_input
                user_log += "\n" + str(chat(user_input))
                #print(user_log)
                user_input = ""

            else:
                user_input += event.unicode
       
        if event.type == pygame.MOUSEWHEEL:
            #print(event.y, scroll)
            if ((scroll - event.y) <= 10) and ((scroll - event.y) >= 0):
                scroll -= event.y

        partial_text(screen, 1240-110, 720-110-100, user_log, get_font(32), scroll)

        pygame.draw.rect(screen, pygame.Color('lightskyblue3'), input_rect) 
        text_surface = get_font(32).render(user_input, True, (255, 255, 255)) 
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 

        input_rect.w = max(100, text_surface.get_width()+10) 
        
        pygame.display.update()


if __name__ == '__main__':
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Chat")

    chat_screen(SCREEN)