import numpy as np
import tensorflow as tf
import keras

def split_sequence_only_y(sequence, n_steps):
	X, y = list(), list()
	for i in range(len(sequence)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the sequence
		if end_ix > len(sequence)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
		X.append(seq_x)
		y.append(seq_y)
	return np.array(X), np.array(y)
 
def split_sequence(data, label, n_steps):
    feature_list = []
    label_list = []
    for i in range(len(data) - n_steps):
        feature_list.append(np.array(data.iloc[i:i+n_steps]))
        label_list.append(np.array(label.iloc[i+n_steps]))
    return np.array(feature_list), np.array(label_list)



class LSTM_model(tf.keras.Model):
    def __init__(self, lstm_layers = [50, 50], nsteps = 3, nfeatures = 1):
        super().__init__()
        self.lstm_layers = lstm_layers
        self.nsteps = nsteps
        self.nfeatures = nfeatures

        self.LSTM1 = keras.layers.LSTM(self.lstm_layers[0], return_sequences=True, activation='relu', input_shape=(self.nsteps, self.nfeatures))
        self.LSTM2 = keras.layers.LSTM(self.lstm_layers[1], activation='relu')
        self.dense1 = keras.layers.Dense(1)

    def call(self, inputs):
        x = self.LSTM1(inputs)
        x = self.LSTM2(x)
        x = self.dense1(x)
        return x
        