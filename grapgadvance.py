from matplotlib import pyplot as plt
ages=[10,10,45,88,99,10,19,1]
#ages=[2,5,60,40,30,45,50,45,43,40,44,60,7,13,57,18,90,77,32,21,20,40]
range=(0,100)
bins=10
#ages2=[12,15,40,30,30,45,50,45,43,40,44,60,71,33,51,18,9,77,32,21,20,100]
bins2=5
plt.hist(ages,bins,range,color='red',histtype='bar',rwidth=0.3)
#plt.hist(ages2,bins2,range,color='blue',histtype='bar',rwidth=0.1)
plt.xlabel('age')
plt.ylabel('no of people')
plt.title('myhistogram')
plt.show()
#####################################################
from keras.models import Sequential
from keras.layers import *
import numpy as np
import pandas as pd
x=pd.read_csv("./Desktop/Logistic_X_Train.csv")
y =pd.read_csv("./Desktop/Logistic_Y_Train.csv")
x_test = pd.read_csv("./Desktop/Logistic_X_Test.csv")
x_test = np.array(x_test)
x = np.array(x)
y = np.array(y)
print(x.shape)
print(y.shape)
x_val = x[:450]
x_train = x[450:]
y_val=y[:450]
y_train = y[450:]
model = Sequential()
model.add(Dense(16,activation="relu",input_shape=(2,)))
model.add(Dense(16,activation="relu"))
model.add(Dense(1,activation="sigmoid"))
model.summary()
model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])
hist = model.fit(x_train,y_train,epochs=60,batch_size=64,validation_data=(x_val,y_val))
import matplotlib.pyplot as plt
a = hist.history["val_loss"]
b = hist.history["val_accuracy"]
c = hist.history["accuracy"]
d =hist.history["loss"]
plt.plot(a,label="val_loss")
plt.plot(b,label="val_accuracy")
plt.plot(c,label="accuracy")
plt.plot(d,label="loss")
plt.legend()
plt.show()
