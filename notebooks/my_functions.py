import pandas as pd

def read_csv_file(filepath):
    df = pd.read_csv(filepath)
    return df


import pandas as pd

def read_csv_file(filepath):
    df = pd.read_csv(filepath)
    return df

def save_csv_file(df, output_filepath):
    df.to_csv(output_filepath, index=False)

data_filepath = "../data/Train_set.csv"
my_data = read_csv_file(data_filepath)

output_filepath = "../data/my_output_data.csv"
save_csv_file(my_data, output_filepath)

# In my_functions.py
def my_function():
    print("Hello from my_function!")
