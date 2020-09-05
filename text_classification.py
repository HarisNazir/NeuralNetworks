import tensorflow as tf
from tensorflow import keras
import numpy as np

data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=10000) #Only take the words that are 10,000 most frequent

print(train_data[0])

word_index = imdb.get_word_index()

word_index = {k:(v+3) for k, v in word_index.items()}