import pandas as pd
from tflearn.data_utils import shuffle
from helper import word_encoder
import random

class preprocess():
    def __init__(self):
        """
        Very small helper class for our bot detector.
        """
        self.w=word_encoder.encoder()

    def remove(self, df, row_name):
        """
        Remove column
        Parameters:
            intput:
                df: Dataframe
                row_name: The name of the row to remove
            ouptput:
                df: The dataframe after removeing the row via name
        """
        del df[row_name]
        return df

    def show_row_names(self,df):
        """
        Parameters:
            input:
                df: Dataframe
            ouptput:
            df.columns: retrun the columns/row names
        """
        return df.columns

    def read(self,file):
        """
        Reads csv file with pandas and create a pandas dataframe
        Parameters:
            input:
                file: The file to convert into an dataframe
            ouptput:
                An pandas dataframe
        """
        return pd.read_csv(file,header=None)

    def add_label(self,df,label):
        """Add a column called label to your dataframe
        Parameters:
            Input:
                df: your pandas dataframe
                label: The kind of label that this dataframe should get
        """
        df=df["Label"]=label
        return df

    def shuffle(self,arrays):
        """Uses the tflearn shuffle command to shuffle the data
        Paramters:
            Input:
                arrays: List of arrays to shuffle
            Output:
                return shuffle(arrays)"""
        return shuffle(arrays)
