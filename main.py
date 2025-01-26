from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Model for input data
class BMICalculatorInput(BaseModel):
    height: float  # Height in meters
    weight: float  # Weight in kilograms

# Endpoint for BMI calculation
@app.post("/calculate_bmi")
def calculate_bmi(data: BMICalculatorInput):
    if data.height <= 0 or data.weight <= 0:
        raise HTTPException(status_code=400, detail="Height and weight must be positive numbers.")
    
    # Formula BMI
    bmi = round(data.weight / (data.height ** 2), 2)

    # BMI Classification
    if bmi < 18.5:
        classification = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        classification = "Normal weight"
    elif 25 <= bmi <= 29.9:
        classification = "Overweight"
    else:
        classification = "Obesity"
    
    return {"bmi": bmi, "classification": classification}
