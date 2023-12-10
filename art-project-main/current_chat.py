from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
time.clock = time.time

chatbot = ChatBot("Chatbot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Hello, I am ART! What's your name? ",
])
trainer.train([
    "How are you",
    "I'm doing great! How about you?",
])
exit_conditions = (":q", "quit", "exit")

def chat(query):
    return chatbot.get_response(query)
    

if __name__ == '__main__':
    while True:
        query = input("> ")
        if query in exit_conditions:
            break
        else:
            print(f" {chatbot.get_response(query)}")
    