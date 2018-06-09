# import required packages 
from sklearn.externals import joblib
import numpy as np 

Xt = np.matrix([71,57,2,50,500,90,95,20])

# reload the model
reloaded_model = joblib.load('model/gbtr_model.gbtr') 

# prediction
prediction = reloaded_model.predict(Xt)[0]
print(prediction)

