# 1. Library imports
import numpy as np

# 2. Values to standardize variables.
scaler_min_max = {'min': np.array([ 32.1, 172. , 13.1]), 'max': np.array([ 59.6, 231. , 21.5])}
scaler_std = {'mean': np.array([0.43028894, 0.49119695, 0.48097776]), 'std': np.array([0.19775223, 0.23784136, 0.23468846])}

# 3. Functions to standardize and predict.
def func_transform(user_input):
    user_input_scaled = (user_input - scaler_min_max['min']) / (scaler_min_max['max'] - scaler_min_max['min'])
    user_input_scaled = (user_input_scaled - scaler_std['mean']) / scaler_std['std']
    return user_input_scaled

def salida_pred(predicted):
    if(predicted[0] == 0):
        prediction="Adelie Penguin (Pygoscelis adeliae)"
    elif(predicted[0] == 1):
        prediction="Chinstrap penguin (Pygoscelis antarctica)"
    else:
        prediction="Gentoo penguin (Pygoscelis papua)"

    predicted = "Prediccion de especie: {}".format(prediction)
    return predicted
