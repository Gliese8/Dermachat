import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer 

# For creating the neurinal network
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.callbacks import EarlyStopping

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

words = []
classes = []
documents = []
ignore_letters = ['?', '!','¡', '¿', '.', ',',':',';','/','|','-','+','@']

# Classify patterns and categories
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# It passes the information to ones or zeros, the according with the words in each category to make the train
training = []
output_empty = [0]*len(classes)
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
random.shuffle(training)
training = np.array(training, dtype=object) 
print(training) 

# Split the data to pass them to the network
train_x = list(training[:,0])
train_y = list(training[:,1])

# Creating the neural network 
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Creating the optimizer and compile it
model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
early_stopping = EarlyStopping(monitor='val_loss', patience=5, verbose=1, restore_best_weights=True)


# Training the model and save it
train_process = model.fit(
    np.array(train_x),
    np.array(train_y),
    epochs=100,
    batch_size=5,
    verbose=1,
    validation_split=0.1, 
    callbacks=[early_stopping]
)
model.save("chatbot_model.h5", train_process)