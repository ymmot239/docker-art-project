import pygame
import os
from pygame import Color
from tkinter import filedialog

pygame.init()

pygame.mixer.init()

def load_music():
    global song, file_label

    song = filedialog.askopenfilename(initialdir=".", title="Select a Song", filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))

    if song:
        pygame.mixer.music.load(song)
        file_name = os.path.basename(song)
        file_label = pygame.font.SysFont(None, 20).render(file_name, True, Color("white"))
        play_music()


def play_music():
    global file_label
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.unpause()
    elif song:
        pygame.mixer.music.load(song)
        file_name = os.path.basename(song)
        file_label = pygame.font.SysFont(None, 20).render(file_name, True, Color("white"))
        pygame.time.delay(500)
        pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def music_player():
    size = (281, 100)
    screen = pygame.display.set_mode(size)
    screen.fill(Color("#222222"))

    load_button = pygame.Surface((80, 40))
    load_button.fill(Color("#444444"))
    load_button_rect = load_button.get_rect()
    load_button_rect.x, load_button_rect.y = 10, 10
    load_button_text = pygame.font.SysFont(None, 20).render("Load", True, Color("white"))
    load_button_text_rect = load_button_text.get_rect()
    load_button_text_rect.x, load_button_text_rect.y = load_button_rect.x + load_button_rect.width // 2, load_button_rect.y + load_button_rect.height // 2

    play_button = pygame.Surface((80, 40))
    play_button.fill(Color("#444444"))
    play_button_rect = play_button.get_rect()
    play_button_rect.x, play_button_rect.y = 100, 10
    play_button_text = pygame.font.SysFont(None, 20).render("Play", True, Color("white"))
    play_button_text_rect = play_button_text.get_rect()
    play_button_text_rect.x, play_button_text_rect.y = play_button_rect.x + play_button_rect.width // 2, play_button_rect.y + play_button_rect.height // 2

    stop_button = pygame.Surface((80, 40))
    stop_button.fill(Color("#444444"))
    stop_button_rect = stop_button.get_rect()
    stop_button_rect.x, stop_button_rect.y = 190, 10
    stop_button_text = pygame.font.SysFont(None, 20).render("Stop", True, Color("white"))
    stop_button_text_rect = stop_button_text.get_rect()
    stop_button_text_rect.x, stop_button_text_rect.y = stop_button_rect.x + stop_button_rect.width // 2, stop_button_rect.y + stop_button_rect.height // 2

    file_label = pygame.font.SysFont(None, 20).render("", True, Color("white"))
    file_label_rect = file_label.get_rect()
    file_label_rect.x, file_label_rect.y = 10, 60

    #clock = pygame.time.Clock()
    #FPS = 60

    background_color = (34, 34, 34)
    line_color = (255, 0, 0)

    load_button_color = Color("#333333")
    play_button_color = Color("#333333")
    stop_button_color = Color("#333333")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if load_button_rect.collidepoint(event.pos):
                    load_music()
                    play_music()
                elif play_button_rect.collidepoint(event.pos):
                    play_music()
                elif stop_button_rect.collidepoint(event.pos):
                    stop_music()

        screen.fill(background_color)

        volume = pygame.mixer.music.get_volume()

        frequency_values = pygame.sndarray.array(pygame.mixer.get_num_channels() * [pygame.mixer.music.get_busy()])
        normalized_values = [abs(i) / 2**15 for i in frequency_values]

        mouse_pos = pygame.mouse.get_pos()
        if load_button_rect.collidepoint(mouse_pos):
            load_button_color = Color("black")
        else:
            load_button_color = Color("#333333")
        if play_button_rect.collidepoint(mouse_pos):
            play_button_color = Color("black")
        else:
            play_button_color = Color("#333333")
        if stop_button_rect.collidepoint(mouse_pos):
            stop_button_color = Color("black")
        else:
            stop_button_color = Color("#333333")

        load_button.fill(load_button_color)
        play_button.fill(play_button_color)
        stop_button.fill(stop_button_color)

        screen.blit(load_button, load_button_rect)
        screen.blit(load_button_text, load_button_text_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(play_button_text, play_button_text_rect)
        screen.blit(stop_button, stop_button_rect)
        screen.blit(stop_button_text, stop_button_text_rect)

        screen.blit(file_label, file_label_rect)

        pygame.display.update()

        #clock.tick(FPS)

if __name__ == '__main__':
	music_player()