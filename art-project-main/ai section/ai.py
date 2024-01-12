from os import listdir
import os
import win32com.client
from os.path import isfile, join
import math
import random

genres = {}
user_change = {}
music_list = {}


def get_genres():
    with open("genre_list.txt","r") as f:
        for x in f.readlines():      
            genres[x.split(":")[0]] = int(x.split(":")[1][:-1])
    return genres


def get_return():
    with open("user_list.txt","r") as f:
        for x in f.readlines():        
            user_change[x.split(":")[0]] = int(x.split(":")[1][:-1])
    return user_change


def edit_weights(original_weight, new_weight):
    change  = {}
    sum = 0
    for key in original_weight:
        change[key] = (new_weight[key] - original_weight[key])/2
        original_weight[key] = original_weight[key] + (new_weight[key] - original_weight[key])/2
        sum += original_weight[key]
    #print(original_weight)
    return original_weight
    

def get_songs():
    with open("genre_to_song.txt","r") as f:
        for x in f.readlines(): 
            part = x.split(" : ")
            if part[0] in music_list:
                music_list[part[0]].append(part[1][:-1])
            else:
                music_list[part[0]] = [part[1][:-1]]
    return music_list


def new_songs(song_list, genre_weights):
    songs = random.choices(list(genre_weights.keys()),weights = genre_weights.values(), k=51)
    songs.sort()
    number = {i:songs.count(i) for i in songs}
    selected = []
    for genre in number:
        if genre in song_list:   
            if number[genre] < len(song_list[genre]):
                holder = {}
                #while len(selected) < sum+number[genre]:
                selected.extend(random.sample(song_list[genre], number[genre]))
            else:
                selected.extend(song_list[genre])
                
    #print(len(selected))
    return selected
    

if __name__ == "__main__":
    print(edit_weights(get_genres(),get_return()))
    #print(get_songs())
    print(new_songs(get_songs(),edit_weights(get_genres(),get_return())))