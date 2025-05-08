import kagglehub
import os
import shutil

def download_bitcoin_data():
    # Download the dataset
    print("Downloading Bitcoin historical data...")
    path = kagglehub.dataset_download("mczielinski/bitcoin-historical-data")
    print(f"Dataset downloaded to: {path}")
    
    # Get the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    # Create a data directory if it doesn't exist
    data_dir = os.path.join(project_root, 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Copy the downloaded files to the data directory
    for file in os.listdir(path):
        src = os.path.join(path, file)
        dst = os.path.join(data_dir, file)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
            print(f"Copied {file} to {data_dir}")
    
    print(f"All files have been copied to {data_dir}")

if __name__ == "__main__":
    download_bitcoin_data() 