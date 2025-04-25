from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os

app = FastAPI()

# File to save the trained model
MODEL_FILE = 'model.pkl'


class QuestionRequest(BaseModel):
    q: str


@app.post("/learn")
async def learn(file: UploadFile = File(...)):
    # Save the uploaded CSV file
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Read the CSV file
    try:
        data = pd.read_csv(file_location)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid CSV file.")

    # Simple assumption: last column is the target variable
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Split data for training/testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Save the trained model
    with open(MODEL_FILE, 'wb') as f:
        pickle.dump(model, f)

    os.remove(file_location)  # Clean up the uploaded file

    return {"message": f"Model trained with accuracy: {accuracy:.2f}"}


@app.get("/ask")
async def ask(request: QuestionRequest):
    # Load the trained model
    if not os.path.exists(MODEL_FILE):
        raise HTTPException(status_code=404, detail="Model not trained yet.")

    with open(MODEL_FILE, 'rb') as f:
        model = pickle.load(f)

    # For now, just return a dummy response (improve with real logic)
    return {"response": f"Your question was: {request.q}"}
