# from fastapi import FastAPI
# import joblib
# from pydantic import BaseModel
# import pandas as pd
# import uvicorn


# # Create an instance of FastAPI
# app = FastAPI(
#     title="Income Status Prediction App",
#     description="Predicts income status based on various factors.",
#     version="1.0.0",
#     contact={
#         "name": "Team Selenium",
#         "email": "teamseleniumapisupport@example.com",
#     }
# )

# # Load model components
# def load_ml_components():
#     with open("./models/model_components.joblib","rb") as file:
#         model_components = joblib.load(file)
#     return model_components


# @app.get("/")
# def get_api_status():
#     return {"status": "API is running"}


# # Create IncomeStatus Features 
# class IncomeStatusFeatures(BaseModel):
#     age: int
#     gender: str
#     education: str
#     marital_status: str
#     race: str
#     is_hispanic: str
#     employment_commitment: str
#     employment_stat: int
#     wage_per_hour: int
#     working_week_per_year: int
#     industry_code: int
#     industry_code_main: str
#     occupation_code: int
#     occupation_code_main: str
#     total_employed: int
#     household_stat: str
#     household_summary: str
#     vet_benefit: int
#     tax_status: str
#     gains: int
#     losses: int
#     stocks_status: int
#     citizenship: str
#     mig_year: int
#     country_of_birth_own: str
#     country_of_birth_father: str
#     country_of_birth_mother: str
#     migration_code_change_in_msa: str
#     migration_code_move_within_reg: str
#     migration_code_change_in_reg: str
#     residence_1_year_ago: str
#     migration_prev_sunbelt:str
#     importance_of_record: float
    
    

# # Create an endpoint for the XGB Classifier
# @app.post("/predict-income-status/xgb_classifier")
# async def income_status_prediction(data:IncomeStatusFeatures):
#     try:
#         # create dataframe from prediction features
#         df = pd.DataFrame([data.model_dump()])
#         # load model components
#         model_components = load_ml_components()
#         # predict income status
#         prediction = model_components["xgb_classifier"].predict(df)
#         # convert predictions to an integer
#         prediction = int(prediction[0])
#         # Inverse predictions to original status
#         inverse_prediction = model_components["encoder"].inverse_transform([prediction])[0]
#         prediction_proba = model_components["xgb_classifier"].predict_proba(df)[0].tolist()

#         response = {"model_used":"XGB Classifier",
#                     "prediction": inverse_prediction,
#                     "prediction_probability":
#                     {"Above limit":round(prediction_proba[0],2),
#                      "Below limit":round(prediction_proba[1],2)}
#                     }
#         return response
#     except Exception as e:
#         return {"error":str(e)}


# @app.post("/predict-income-status/gradient_boosting")
# async def income_status_prediction(data:IncomeStatusFeatures):
#     try:
#         # create dataframe from prediction features
#         df = pd.DataFrame([data.model_dump()])
#         # load model components
#         model_components = load_ml_components()
#         # predict income status
#         prediction = model_components["gradient_boost"].predict(df)
#         # convert predictions to an integer
#         prediction = int(prediction[0])
#         # Inverse predictions to original status
#         inverse_prediction = model_components["encoder"].inverse_transform([prediction])[0]
#         prediction_proba = model_components["gradient_boost"].predict_proba(df)[0].tolist()

#         response = {"model_used":"Gradient Boosting Algorithm",
#                     "prediction": inverse_prediction,
#                     "prediction_probability":
#                     {"Above limit":round(prediction_proba[0],2),
#                      "Below limit":round(prediction_proba[1],2)}
#                     }
#         return response
#     except Exception as e:
#         return {"error":str(e)}
    

# if __name__ == "__main__":
#     uvicorn.run("api.py",reload=True)


from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd
import uvicorn

# Create an instance of FastAPI
app = FastAPI(
    title="Income Status Prediction App",
    description="Predicts income status based on various factors.",
    version="1.0.0",
    contact={
        "name": "Team Selenium",
        "email": "teamseleniumapisupport@example.com",
    }
)

# Load model components
def load_ml_components():
    with open("./models/model_components.joblib", "rb") as file:
        model_components = joblib.load(file)
    return model_components

@app.get("/")
def get_api_status():
    return {"status": "API is running"}

# Create IncomeStatus Features 
class IncomeStatusFeatures(BaseModel):
    age: int
    gender: str
    education: str
    marital_status: str
    race: str
    is_hispanic: str
    employment_commitment: str
    employment_stat: int
    wage_per_hour: int
    working_week_per_year: int
    industry_code: int
    industry_code_main: str
    occupation_code: int
    occupation_code_main: str
    total_employed: int
    household_stat: str
    household_summary: str
    vet_benefit: int
    tax_status: str
    gains: int
    losses: int
    stocks_status: int
    citizenship: str
    mig_year: int
    country_of_birth_own: str
    country_of_birth_father: str
    country_of_birth_mother: str
    migration_code_change_in_msa: str
    migration_code_move_within_reg: str
    migration_code_change_in_reg: str
    residence_1_year_ago: str
    migration_prev_sunbelt: str
    importance_of_record: float

# Create an endpoint for the XGB Classifier
@app.post("/predict-income-status/xgb_classifier")
async def income_status_prediction(data: IncomeStatusFeatures):
    try:
        # create dataframe from prediction features
        df = pd.DataFrame([data.model_dump()])  # Use model_dump() for Pydantic v2.x
        # load model components
        model_components = load_ml_components()
        # predict income status
        prediction = model_components["xgb_classifier"].predict(df)
        # convert predictions to an integer
        prediction = int(prediction[0])
        # Inverse predictions to original status
        inverse_prediction = model_components["encoder"].inverse_transform([prediction])[0]
        prediction_proba = model_components["xgb_classifier"].predict_proba(df)[0].tolist()

        response = {
            "model_used": "XGB Classifier",
            "prediction": inverse_prediction,
            "prediction_probability": {
                "Above limit": round(prediction_proba[0], 2),
                "Below limit": round(prediction_proba[1], 2)
            }
        }
        return response
    except Exception as e:
        return {"error": str(e)}

# Create an endpoint for the Gradient Boosting Classifier
@app.post("/predict-income-status/gradient_boosting")
async def income_status_prediction(data: IncomeStatusFeatures):
    try:
        # create dataframe from prediction features
        df = pd.DataFrame([data.model_dump()])  # Use model_dump() for Pydantic v2.x
        # load model components
        model_components = load_ml_components()
        # predict income status
        prediction = model_components["gradient_boost"].predict(df)
        # convert predictions to an integer
        prediction = int(prediction[0])
        # Inverse predictions to original status
        inverse_prediction = model_components["encoder"].inverse_transform([prediction])[0]
        prediction_proba = model_components["gradient_boost"].predict_proba(df)[0].tolist()

        response = {
            "model_used": "Gradient Boosting Algorithm",
            "prediction": inverse_prediction,
            "prediction_probability": {
                "Above limit": round(prediction_proba[0], 2),
                "Below limit": round(prediction_proba[1], 2)
            }
        }
        return response
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)
