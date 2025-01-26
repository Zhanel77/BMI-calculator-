# BMI Calculator API

## Overview
This project provides a RESTful API for calculating Body Mass Index (BMI) using **FastAPI**. It allows users to input height and weight and receive their BMI along with a classification (e.g., "Underweight", "Normal weight", "Overweight", "Obesity").

## Requirements
- Python 3.8 or higher
- Installed dependencies:
  - `fastapi`
  - `uvicorn`

## Installation and Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

2. Install dependencies:

bash
pip install fastapi uvicorn
Save your API code in a file named main.py.

3. Start the API server:

bash
uvicorn main:app --reload
Open the Swagger UI for testing:
http://127.0.0.1:8000/docs

API Usage
Endpoint
POST /calculate_bmi

Request
Content-Type: application/json

# Testing
Open Swagger UI:
(http://127.0.0.1:8000/docs)

- Open this path in the browser and your BMI will start.
- Use the "Try" button to send test requests. 
- Enter the data and click "Run". And you will be able to see the output.


Example Body:
json
{
  "height": 1.75,
  "weight": 70
}

Response
Success:
json
{
  "bmi": 22.86,
  "classification": "Normal weight"
}

Error (invalid input):
json
{
  "detail": "Height and weight must be positive numbers."
}