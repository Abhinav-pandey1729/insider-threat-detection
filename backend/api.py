from backend.model import load_model, predict  
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()
model = load_model()

class UserActivity(BaseModel):
    user_id: int
    file_access_freq: int
    logon_freq: int
    http_freq: int

@app.post("/predict/")
def predict_threat(user_activity: UserActivity):
    data = [[user_activity.file_access_freq, user_activity.logon_freq, user_activity.http_freq]]
    prediction = model.predict(data)
    return {"threat": "Suspicious" if prediction[0] == -1 else "Normal"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
