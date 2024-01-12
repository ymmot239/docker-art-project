import pygame
import os
import re
import math
import inspect
import sys
from os import listdir
from os.path import isfile, join
from pygame import Color

pygame.init()

pygame.mixer.init()

def save_exit(input_change):
    f = open("demofile.txt", "w+")
    # open and read the file after the overwriting:
    def yes_or_no():
        answer = input("Please enter yes or no ")
        while answer.lower() != 'yes' and answer.lower != 'no':
            answer = input("Please enter yes or no ")
        return answer.lower()

    yes_or_no()
    f.write("Woops! I have deleted the content!")
    f.close()





def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/marlboro.ttf", size)


def get_music():
    mypath = "./music"
    filelist = next(os.walk(mypath))[1]
    onlyfiles = {}
    for x in filelist:
        newpath = mypath + "/" + x
        #onlyfiles += [newpath + "/" + f for f in listdir(newpath) if isfile(join(newpath, f))]
        for f in listdir(newpath):
             if isfile(join(newpath,f)):
                 f_edit = re.sub(r'[^a-zA-Z\d\s:]',"",f[:-4]).strip()
                 if len(f_edit) > 30:
                     f_edit = f_edit[:30] + "~"
                 onlyfiles[f_edit] = newpath+"/"+f
    return onlyfiles


def show_music(screen, dict, size):
    
    font = get_font(size)
    keys = [key for key in dict]
    rects = []

    top_spacer = 110
    bottom_spacer = 100
    left_spacer = 10
    text_width_modifier = 14

    lines = int((screen.get_size()[1] - top_spacer - bottom_spacer) / size)
    columns = int((screen.get_size()[0] - left_spacer) / (size*text_width_modifier))

    for cols in range(columns):
        for rows in range(lines):
            if rows+cols*lines >= len(keys):
                break

            word_surface = font.render(keys[rows+cols*lines], 0, 'White')
            word_rect = screen.blit(word_surface, (cols*size * text_width_modifier + left_spacer, 
                                                   rows*size + top_spacer))
            rects += [word_rect]

    return rects


def play_music(song):
    global file_label

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()

    elif song:
        pygame.mixer.music.load(song)
        file_name = os.path.basename(song)
        file_label = pygame.font.SysFont(None, 20).render(file_name, True, Color("white"))
        pygame.time.delay(500)
        pygame.mixer.music.play()


def music_player(screen):
    
    music_list = get_music()
    
    selected = pygame.Surface((0,0),pygame.SRCALPHA)
    selected_rect = selected.get_rect()

    start_button = pygame.Surface((150, 60),pygame.SRCALPHA)
    start_button.fill((0,255,0,255))
    start_button_rect = start_button.get_rect()
    start_button_rect.centerx, start_button_rect.y = 420, 630
    start_button_text = pygame.font.SysFont(None, 60).render("Start", True, Color("white"))
    start_button.blit(start_button_text, start_button_text.get_rect(center=(start_button_rect.width//2, start_button_rect.height//2)))


    stop_button = pygame.Surface((150, 60),pygame.SRCALPHA)
    stop_button.fill((255,0,0,100))
    stop_button_rect = stop_button.get_rect()
    stop_button_rect.centerx, stop_button_rect.y = 840, 630
    stop_button_text = pygame.font.SysFont(None, 60).render("Stop", True, Color("white"))
    stop_button.blit(stop_button_text, stop_button_text.get_rect(center=(stop_button_rect.width//2, stop_button_rect.height//2)))

    playing_music = False
    selected_music = None  

    user_list = []
    file = open("song_counter.txt","a",encoding = "utf-8")

    while 1:
        screen.fill(Color("#4f42b5"))

        MUSIC_TEXT = get_font(45).render("This is the MUSIC screen.", True, "White")
        MUSIC_RECT = MUSIC_TEXT.get_rect(center=(640, 50))
        screen.blit(MUSIC_TEXT, MUSIC_RECT)

        rects = show_music(screen, music_list, 30)
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

        screen.blit(selected, selected_rect)

        screen.blit(start_button, start_button_rect)
        screen.blit(stop_button, stop_button_rect)

        if event.type == pygame.QUIT:
            for x in user_list:
                file.write(x+"\n")
            file.close()
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if holder_rect.collidepoint(cursor):
                pygame.mixer.music.stop()
                for x in user_list:
                    file.write(x+"\n")
                file.close()
                return

            if start_button_rect.collidepoint(cursor) and not playing_music:
                if selected_music != None:
                    play_music(selected_music)
                    playing_music = True
                    start_button.fill((0,255,0,100))
                    stop_button.fill((255,0,0,255))
                    start_button.blit(start_button_text, start_button_text.get_rect(center=(start_button_rect.width//2, start_button_rect.height//2)))
                    stop_button.blit(stop_button_text, stop_button_text.get_rect(center=(stop_button_rect.width//2, stop_button_rect.height//2)))

            if stop_button_rect.collidepoint(cursor) and playing_music:
                pygame.mixer.music.stop()
                playing_music = False
                stop_button.fill((255,0,0,100))
                start_button.fill((0,255,0,255))
                start_button.blit(start_button_text, start_button_text.get_rect(center=(start_button_rect.width//2, start_button_rect.height//2)))
                stop_button.blit(stop_button_text, stop_button_text.get_rect(center=(stop_button_rect.width//2, stop_button_rect.height//2)))

            for x in range(len(rects)):
                item = rects[x]
                if item.collidepoint(cursor):
                    key = list(music_list.keys())[x]
                    value = music_list[key]
                    selected_music = value
                    selected = pygame.Surface((item.width, item.height),pygame.SRCALPHA)
                    selected.fill((81,114,161,100))
                    selected_rect = selected.get_rect(topleft=(item.x, item.y))

                    user_list.append(key)

                    pygame.mixer.music.stop()
                    playing_music = False
                    stop_button.fill((255,0,0,100))
                    start_button.fill((0,255,0,255))
                    start_button.blit(start_button_text, start_button_text.get_rect(center=(start_button_rect.width//2, start_button_rect.height//2)))
                    stop_button.blit(stop_button_text, stop_button_text.get_rect(center=(stop_button_rect.width//2, stop_button_rect.height//2)))

        pygame.display.update()


if __name__ == "__main__":

    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Music")
    
    music_player(SCREEN)


