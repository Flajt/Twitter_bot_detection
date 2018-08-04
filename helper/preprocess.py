import pandas as pd

class preprocess():
    def __init__(self):
        """
        Very small helper class for our bot detector.
        """

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
        return pd.read_csv()
