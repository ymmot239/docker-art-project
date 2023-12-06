import time
from music_player import music_player
from current_chat import chat

menu_options = (1, 2, 3)

while True:
    print()
    print('Hello! My name is ART! What would you like to do today? ')
    print()
    print('Options:')
    print('1 = Chat')
    print('2 = Listen to Music')
    print('3 = Watch a Movie')
    print()

    user_input = input('Enter an option: ')
    print('you input ' + user_input)

    if int(user_input) == 1:
        chat()
        #pass

    elif int(user_input) == 2:
        music_player()

    elif int(user_input) in menu_options:
        break

    else:
        print("I'm sorry, I cannot help you with that at the moment")