from os import listdir
import os
import win32com.client
from os.path import isfile, join
import math
import random


def songs_to_genre_list(user_list_path, genre_to_song_path):
    song_to_genre = {}
    with open(genre_to_song_path, "r") as f:
        for x in f.readlines():
            holder = x.split(" : ")
            song_to_genre[holder[1]] = holder[0]
    genre_list = []
    with open(user_list_path, "r") as f:
        for x in f.readlines():
            genre_list.append(song_to_genre[x])
    return genre_list
        
        
def list_to_weights(genre_list,master_list):
    genres = {}
    sum = 0
    with open(master_list,"r") as f:
        for x in f.readlines():
            genres[x[:-1]] = int(genre_list.count(x[:-1])/len(genre_list)*100)
            sum += int(genre_list.count(x[:-1])/len(genre_list)*100)
    if sum < 100:
        genres[list(genres.keys())[0]] += 100-sum        
    return genres

def weights_to_file(weights, paths):
    with open(paths + "\\genre_list.txt","w+") as f:
        for x in list(weights.keys()):
            f.write(x + ":" + str(weights[x]) + "\n")
if __name__ == "__main__":
    weight_list = songs_to_genre_list("..\\song_counter.txt",".\\genre_to_song.txt")
    weighted = list_to_weights(weight_list,"genres.txt")
    weights_to_file(weighted, ".\\")