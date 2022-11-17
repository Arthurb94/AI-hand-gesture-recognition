from keras import models
from keras import layers
from keras import optimizers
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
from tensorflow.keras.utils import to_categorical


model = models.Sequential()

# création du réseau de neronnes
model.add(layers.Dense(256, activation='relu', input_shape=(63,)))
model.add(layers.Dense(256, activation='relu') )
model.add(layers.Dense(10,activation ='softmax'))

#assemblage des couches de neronnes
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#lecture des données
data = pd.read_csv('bdd/final.csv', index_col= 0)
test_size = int(len(data) * 0.2)
train = train = data.iloc[:-test_size,:].copy() 
test = data.iloc[-test_size:,:].copy()

#sélection des données d'entrainement 
x_train = train.iloc[:,0:-1]
y_train = train.iloc[:,-1]

#sélection des données de validation
x_test = test.iloc[:,0:-1]
y_test = test.iloc[:,-1]

#convertion en matrice np
arr_x_train = x_train.to_numpy()
arr_y_train = y_train.to_numpy()
arr_y_test = y_test.to_numpy()
arr_x_test = x_test.to_numpy()
y_train = to_categorical(arr_y_train, dtype="uint8")
y_test = to_categorical(arr_y_test, dtype="uint8")

#lancement de l'entrainement du model
model.fit(arr_x_train, y_train,validation_data=(arr_x_test,y_test), epochs=10, validation_steps=7, workers=4)

score = model.evaluate(arr_x_test, y_test, verbose=0)
print (score)
model.save('model_final.h5')