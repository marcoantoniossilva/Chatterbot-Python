from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONVERSATION_SETTINGS=[
    "C:\\Users\\Win10\\Documents\\GitHub\\Chatterbot-Python\\conversations\\greetings.json",
    "C:\\Users\\Win10\\Documents\\GitHub\\Chatterbot-Python\\conversations\\basic_information.json",
    "C:\\Users\\Win10\\Documents\\GitHub\\Chatterbot-Python\\conversations\\product_compositions.json",
    "C:\\Users\\Win10\\Documents\\GitHub\\Chatterbot-Python\\conversations\\product_prices.json"]

def initialize():
    global bot
    global trainer

    bot = ChatBot("Robô de atendimento da Linda Joia")
    trainer = ListTrainer(bot)

def load_conversations():
    conversations =[]

    for setting_file in CONVERSATION_SETTINGS:
        with open(setting_file, 'r',encoding="utf-8") as file:
            configured_conversations = json.load(file)
            conversations.append(configured_conversations["conversations"])

            file.close()
    

    return conversations;


def train_bot(conversations):
    global trainer

    for conversation in conversations:
        for message_response in conversation:
            messages = message_response["messages"]
            response = message_response["response"]

            print("Treinando o robô para responder a:'",messages, "' Com a resposta'",response,"'")
            for message in messages:
                trainer.train([message,response])


if __name__ == "__main__":
    initialize()
    conversations = load_conversations()
    if conversations:
        train_bot(conversations)
