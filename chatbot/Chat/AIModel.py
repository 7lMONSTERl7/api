
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from .data_container import Data

class AIModel:
    def __init__(self):
        self.chatbot = ChatBot("MultilingualChatBot")
        self.trained = False

    def train_model(self):
        if not self.trained:
            trainer = ChatterBotCorpusTrainer(self.chatbot)
            trainer.train("/home/monster/Desktop/chatbot/data/arabic")
            trainer.train("/home/monster/Desktop/chatbot/data/english")
            trainer.train("/home/monster/Desktop/chatbot/data/french")
            self.trained = True
            print("Chatbot has been trained in Arabic, English, and French.")
        else:
            print("Chatbot has already been trained.")

    def load_model(self):
        if not self.trained:
            try:
                # Load your trained model here
                self.chatbot.storage.read_only = True
                self.trained = True
                print("Trained model loaded successfully.")
            except:
                print("No trained model found. Please train the model first.")
        else:
            print("Model already loaded.")

    def model(self, prompt, *args):
        if Data().respond(prompt):
            response = Data().respond(prompt)
        else:
            response = self.chatbot.get_response(prompt)
        return response
