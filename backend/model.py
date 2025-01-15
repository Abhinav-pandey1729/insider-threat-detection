from sklearn.ensemble import IsolationForest
import pickle

def train_model(features):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(features.drop("user_id", axis=1))

    with open("isolation_forest.pkl", "wb") as f:
        pickle.dump(model, f)
    return model

def load_model():
    with open("isolation_forest.pkl", "rb") as f:
        return pickle.load(f)

if __name__ == "__main__":
    from feature_engineering import generate_features
    from data_loader import load_all_data

    data = load_all_data()
    features = generate_features(data)
    train_model(features)
    print("Model trained and saved.")
