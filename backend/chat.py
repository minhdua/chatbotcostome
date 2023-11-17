import json
import random

import torch
from models.common.normalize_text import normalize_text
from models.enum import ResponseMessage
from models.nlp.intent_model import Intent
from module import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
FILE = "backend/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

class Intents:
    def __init__(self, tag, patterns, responses):
        self.tag = tag
        self.patterns = patterns
        self.responses = responses
    def serialize(self):
        return {
            "tag": self.tag,
            "patterns": self.patterns,
            "responses": self.responses
        }


#============================================================
# Get Intents                                              #
#============================================================
def get_intents():
    intent_array = []
    intents = Intent.query.all()
    for intent in intents:
        patterns = [''.join(i.pattern_text) for i in intent.patterns]
        responses = [''.join(i.response_text) for i in intent.responses]
        intent_array.append(Intents(intent.tag, patterns, responses).serialize()) 
    return {"intents":intent_array}



#============================================================
# Get Response For Client Request                           #
#============================================================
def get_response(msg):
    data_intents = get_intents()
    sentence = tokenize(msg)
    
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    
    try:
        if prob.item() > 0.75:
            for intent in data_intents['intents']:
                if normalize_text(tag) == normalize_text(intent["tag"]):
                    return random.choice(intent['responses'])
    except Exception:
        return ResponseMessage.MESSAGE01.value
    
    
    return ResponseMessage.MESSAGE02.value
#============================================================

if __name__ == "__main__":
    print("Hãy tán gẫu nào! (gõ 'quit' để thoát)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)