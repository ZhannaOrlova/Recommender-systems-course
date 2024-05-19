'''Kaggle data set loading and processing'''

from data_loader import Dataset

data = Dataset('kaggle datasets download -d grouplens/movielens-20m-dataset?select=rating.csv')

for i in data.dataset:
    print(i)
