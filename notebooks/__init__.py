import os
import pandas as pd

# In init.py and mod1.py, import the load_data function from data_loader.py: (ChatGPT3):
from notebooks.utils.data_loader import load_data


# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'Train_set.csv')))
