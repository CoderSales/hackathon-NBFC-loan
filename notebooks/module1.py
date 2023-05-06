# from NBFC_loan import data, df
import pandas as pd

# https://stackoverflow.com/questions/50767663/global-dataframe-across-files-in-a-project

# def init():

# def isna_checker(data=data, col=col):
def isna_checker(data=data,col=col,*args,**kwargs):
    """
    function to check if the count in each col of data is 0. 
    """
    # global GDF
    # GDF=pd.DataFrame()
    data = pd.read_csv('../data/Train_set.csv')
    df = data.copy()
    dc=data[col]
    for col in data.columns:
        print(data[col].head(2))
    df_isna=df.isna().sum() # full dataframe
    found_na=False
    # for i in df_isna.keys(): # take 1 key at a time out of just the keys
    #     if df_isna==0:
    #         pass
    # inform user
    # if found_na==False:
    #     print('no na values in data')
    # else:
    #     print('the following columns have na values:')


# https://youtu.be/oOn7eOKQXRY?t=203
