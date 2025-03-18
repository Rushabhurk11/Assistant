import json
import pickle
import tensorflow as tf
from pyexpat import model
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np


with open("intents.json") as file:
    data = json.load(file)

model = keras.models.load_model("chat_model.h5")

with open("tokenizer.pkl", "rb") as f:
    Tokenizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder = pickle.load(encoder_file)

while True:
    input_text = input("Enter your command-> ")
    padded_sequences = pad_sequences(Tokenizer.texts_to_sequences([input_text]), truncating='post', maxlen=20)
    result = model.predict(padded_sequences)
    tag = label_encoder.inverse_transform([np.argmax(result)])

    for i in data["intents"]:
        if i["tag"] == tag:
            print(random.choice(i["responses"]))
            break
