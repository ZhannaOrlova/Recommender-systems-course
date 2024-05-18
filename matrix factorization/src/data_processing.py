'''Kaggle data set loading and processing'''

from data_loader import Dataset

data = Dataset('kaggle datasets download -d grouplens/movielens-20m-dataset')

for i in data.dataset:
    print(i)
