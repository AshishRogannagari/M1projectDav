import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns

class eda:
    def __init__(self, df):
        """
        Initialize an EDA (Exploratory Data Analysis) object with a DataFrame.

        Parameters:
        df (pandas.DataFrame): The DataFrame to be analyzed.
        """
        self.df = df

    def display_dataframe(self):
        """
        Display the entire DataFrame.

        Returns:
        pandas.DataFrame: The input DataFrame.
        """
        return self.df

    def Head(self, a=5):
        """
        Return the first 'a' rows of the DataFrame.

        Parameters:
        a (int, optional): The number of rows to display. Default is 5.

        Returns:
        pandas.DataFrame: The first 'a' rows of the DataFrame.
        """
        return self.df.head(a)

    def Info(self):
        """
        Display a concise summary of the DataFrame's info, including data types, non-null counts, and memory usage.

        Returns:
        None
        """
        return self.df.info()

    def drop_null_col(self):
        """
        Drop specified columns with null values from the DataFrame in place.

        Note: This function modifies the DataFrame in place and does not return a new DataFrame.

        Returns:
        None
        """
        return self.df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

    def check_null_sum(self):
        """
        Return the count of null values for each column in the DataFrame.

        Returns:
        pandas.Series: A Series containing the count of null values for each column.
        """
        return pd.isnull(self.df).sum()

    def drop_null(self):
        """
        Drop rows with null values from the DataFrame in place.

        Note: This function modifies the DataFrame in place and does not return a new DataFrame.

        Returns:
        None
        """
        return self.df.dropna(inplace=True)

    def columns_names(self):
        """
        Return the names of the columns in the DataFrame.

        Returns:
        Index: A pandas Index object containing column names.
        """
        return self.df.columns

    def Describe(self):
        """
        Generate descriptive statistics for the numerical columns in the DataFrame.

        Returns:
        pandas.DataFrame: A summary of basic statistics for numerical columns.
        """
        return self.df.describe()

    def Describe_column_name(self, colname):
        """
        Generate descriptive statistics for a specific column in the DataFrame.

        Parameters:
        colname (str): The name of the column for which you want statistics.

        Returns:
        pandas.Series: A summary of basic statistics for the specified column.
        """
        return self.df[colname].describe()

    
    
    
