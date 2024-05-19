'''Downloads temporary datasets from Kaggle'''

import os
import zipfile
import pandas as pd
from datetime import date


class Dataset:
    def __init__(self, API_command):
        # Download the dataset
        os.system(API_command)
        
        # Extract the zip filename from the command
        self.name = API_command.split('-d ')[1].split(' ')[0]
        self.zip_filename = self.name.split('/')[-1] + '.zip'
        
        self.Open()
        os.remove(self.zip_filename)
    
    def Open(self):
        self.dataset = []
        
        with zipfile.ZipFile(self.zip_filename, 'r') as zip_ref:
            filenames = zip_ref.namelist()
            zip_ref.extractall()
        
        for file in filenames:
            if file.endswith('rating.csv'):
                self.dataset.append(pd.read_csv(file, nrows=10000))
            else:
                self.dataset.append(pd.read_csv(file))
        self.filenames = filenames

# Code to run only if this script is executed directly
if __name__ == "__main__":
    data = Dataset('kaggle datasets download -d grouplens/movielens-20m-dataset')
    
    for df in data.dataset:
        print(df.head())  # Printing only the first few rows for verification
