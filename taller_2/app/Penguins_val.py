# 1. Library imports
from pydantic import BaseModel

# 2. Class for models.
class Penguins(BaseModel):
    studyName:str
    Sample_Number:float
    Region:str
    Island:str
    Stage:str
    Individual_ID:str
    Clutch_Completion:str
    Date_Egg:str
    Culmen_Length_mm:float
    Culmen_Depth_mm:float
    Flipper_Length_mm:float
    Body_Mass_g:float
    Sex:str
    Delta_15_N:float
    Delta_13_C:float
    Comments:str
