import subprocess

def train_model():
    print("Training the model...")
    subprocess.run(["python", "backend/model.py"])

def run_api():
    print("Starting the API server...")
    subprocess.run(["uvicorn", "backend.api:app", "--reload", "--host", "127.0.0.1", "--port", "8000"])

if __name__ == "__main__":
    train_model()
    run_api()
