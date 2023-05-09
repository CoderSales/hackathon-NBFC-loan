# mod1.py

def read_csv_file(filepath):
    """
    function to read the csv file
    """
    import pandas as pd
    data=pd.read_csv(filepath)
    return data

def save_csv_file(data, filepath):
    """
    function to save the given data to a csv file
    """
    data.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

def isna_checker(data, col):
    """
    function to check if the count in each col of data is 0. 
    """
    dc = data[col]
    df_isna = dc.isna().sum()
    found_na = False
    if df_isna == 0:
        pass
    else:
        found_na = True
        print(f"Column '{col}' has {df_isna} missing values")
    return found_na
    # for i in df_isna.keys(): # take 1 key at a time out of just the keys
    #     if df_isna==0:
    #         pass
    # inform user
    # if found_na==False:
    #     print('no na values in data')
    # else:
    #     print('the following columns have na values:')

def col_looper(data):
    """
    function to loop over all columns and check for NA values
    """
    for col in data.columns:
        print(data[col].head(2))
        isna_checker(data=data, col=col)

def col_describer(df):
    for col in list(df):
        print(df[col].describe())

__all__ = ['read_csv_file', 'save_csv_file', 'isna_checker', 'col_looper', 'col_describer']
