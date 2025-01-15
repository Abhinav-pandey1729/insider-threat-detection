import pandas as pd

def generate_features(datasets):
    # File access frequency
    file_access_freq = datasets["file"].groupby("user_id")["file_accessed"].count().reset_index()
    file_access_freq.columns = ["user_id", "file_access_freq"]

    # Login frequency
    logon_freq = datasets["logon"].groupby("user_id")["logon_time"].count().reset_index()
    logon_freq.columns = ["user_id", "logon_freq"]

    # HTTP requests frequency
    http_freq = datasets["http"].groupby("user_id")["url"].count().reset_index()
    http_freq.columns = ["user_id", "http_freq"]

    # Merge features
    features = pd.merge(file_access_freq, logon_freq, on="user_id", how="outer")
    features = pd.merge(features, http_freq, on="user_id", how="outer").fillna(0)

    return features

if __name__ == "__main__":
    from data_loader import load_all_data
    data = load_all_data()
    features = generate_features(data)
    print(features.head())
