# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Penguins_val import Penguins
import pickle
from my_functions import func_transform, salida_pred
from enum import Enum

# 2. Create the app object
app = FastAPI()

dt = pickle.load(open('cl_dt.pkl', 'rb'))
lr = pickle.load(open('cl_lr.pkl', 'rb'))

# 3. Index route, opens automatically on http://127.0.0.0:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence

class ModelOptions(str, Enum):
    mod_1 = "Logistic Regression"
    mod_2 = "Classification Tree"

@app.post('/predict')
def predict_penguins(data:Penguins, model: ModelOptions):
    data = data.dict()
    studyName = data['studyName']
    Sample_Number = data['Sample_Number']
    Region = data['Region']
    Island = data['Island']
    Stage = data['Stage']
    Individual_ID = data['Individual_ID']
    Clutch_Completion = data['Clutch_Completion']
    Date_Egg = data['Date_Egg']
    Culmen_Length_mm = data['Culmen_Length_mm']
    Culmen_Depth_mm = data['Culmen_Depth_mm']
    Flipper_Length_mm = data['Flipper_Length_mm']
    Body_Mass_g = data['Body_Mass_g']
    Sex = data['Sex']
    Delta_15_N = data['Delta_15_N']
    Delta_13_C = data['Delta_13_C']
    Comments = data['Comments']

   # Estandarizar variables
    user_input = [Culmen_Length_mm, Flipper_Length_mm, Culmen_Depth_mm]
    user_input_scaled = func_transform(user_input)

    # Seleccionar modelo
    if model == ModelOptions.mod_1:
        out_model = salida_pred(lr.predict([user_input_scaled]))
    elif model == ModelOptions.mod_2:
        out_model = salida_pred(dt.predict([user_input_scaled]))

    return {
        out_model
    }

# 5. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8989)
