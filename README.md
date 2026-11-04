
# Insurance Premium Prediction API

A machine learning project built to practice FastAPI.

## About the Project

This project predicts insurance premium categories using a Random Forest model trained on a synthetic (toy) dataset created by me.

## Technologies Used

- Python
- FastAPI
- Scikit-learn
- Pandas
- Random Forest

## Features

- Predict insurance premium categories
- Validate user inputs using Pydantic
- Provide predictions through a REST API
- Interactive API documentation using Swagger UI

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open API documentation:

http://127.0.0.1:8000/docs

## Note

This project is for learning and practice. The model was trained on sy
nthetic data and is not intended for real-world insurance decisions.
