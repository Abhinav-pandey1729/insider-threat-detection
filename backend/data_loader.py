import kagglehub
import time

def download_dataset(retries=3, delay=5):
    for attempt in range(retries):
        try:
            print(f"Attempt {attempt + 1} to download dataset...")
            path = kagglehub.dataset_download("mrajaxnp/cert-insider-threat-detection-research")
            print("Dataset downloaded successfully.")
            return path
        except Exception as e:
            print(f"Download failed: {e}")
            if attempt < retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Failed to download dataset after multiple attempts.")
                raise e
