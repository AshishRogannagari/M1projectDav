import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns


class Int:
    def __init__(self,df):
        """
        Initialize an instance of the Int class with a DataFrame.

        Parameters:
        - df: pandas.DataFrame
            The DataFrame to work with.
        """
        self.df = df

    def countplot(self,colname = None, hue = None):
        """
        Create a countplot using Seaborn for a specified column.

        Parameters:
        - colname: str, optional
            The name of the column to plot.
        - hue: str, optional
            The name of the column to use for color differentiation.

        This function uses Seaborn to create a countplot of the specified column.

        """        
        ax = sns.countplot(x = colname, data = self.df)
        for bars in ax.containers:
            ax.bar_label(bars)
        plt.xticks(rotation = 90)

    def countplot_matplotlib(self, colname=None, hue=None):
        """
        Create a countplot using Matplotlib for a specified column.

        Parameters:
        - colname: str, optional
            The name of the column to plot.
        - hue: str, optional
            The name of the column to use for color differentiation.

        This function uses Matplotlib to create a countplot of the specified column.

        """
        counts = self.df[colname].value_counts()

        # Plotting with Matplotlib
        fig, ax = plt.subplots(figsize=(12, 8))
        bars = ax.bar(counts.index, counts.values, color=plt.cm.get_cmap('tab10').colors)

        # Adding labels to the bars
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

        ax.set_title(f'Count of {colname.capitalize()} (Matplotlib)')
        ax.set_xlabel(colname.capitalize())
        ax.set_ylabel('Count')
        ax.tick_params(axis='x', rotation=90)

        plt.tight_layout()
        plt.show()


    def barchart(self,x = None, y = None, hue = None):

        """
        Create a bar chart using Seaborn to visualize a relationship between columns.

        Parameters:
        - x: str, optional
            The name of the x-axis column.
        - y: str, optional
            The name of the y-axis column.
        - hue: str, optional
            The name of the column to use for color differentiation.

        This function uses Seaborn to create a bar chart to visualize the relationship between columns.

        """
        sales_gen = self.df.groupby([x], as_index=False)[y].sum().sort_values(by=y, ascending=False)
        sns.barplot(x = x, y= y ,data = sales_gen, hue = hue)
        plt.xticks(rotation = 90)

    def barchart_matplotlib(self, x=None, y=None, hue=None):

        """
        Create a bar chart using Matplotlib to visualize a relationship between columns.

        Parameters:
        - x: str, optional
            The name of the x-axis column.
        - y: str, optional
            The name of the y-axis column.
        - hue: str, optional
            The name of the column to use for color differentiation.

        This function uses Matplotlib to create a bar chart to visualize the relationship between columns.

        """
        sales_gen = self.df.groupby([x], as_index=False)[y].sum().sort_values(by=y, ascending=False)

        # Plotting with Matplotlib
        fig, ax = plt.subplots(figsize=(12, 8))
        bars = ax.bar(sales_gen[x], sales_gen[y], color=plt.cm.get_cmap('tab20').colors)
        
        # Adding legend if hue is provided
        if hue is not None:
            legend_labels = self.df[hue].unique()
            ax.legend(bars, legend_labels, loc='upper left', bbox_to_anchor=(1, 1))

        ax.set_title(f'{y.capitalize()} by {x.capitalize()} (Matplotlib)')
        ax.set_xlabel(x.capitalize())
        ax.set_ylabel(y.capitalize())
        ax.tick_params(axis='x', rotation=90)
        
        plt.tight_layout()
        plt.show()

    def bar(self, x = None, y = None):

        """
        Create a bar chart using Seaborn for the sum of values in the specified columns.

        Parameters:
        - x: str, optional
            The name of the x-axis column.
        - y: str, optional
            The name of the y-axis column.

        This function uses Seaborn to create a bar chart for the sum of values in the specified columns.

        """
        fig1, ax1 = plt.subplots(figsize=(12,7))
        self.df.groupby(x)[y].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

        
    def bar_matplotlib(self, x=None, y=None):
        """
        Create a bar chart using Matplotlib for the sum of values in the specified columns.

        Parameters:
        - x: str, optional
            The name of the x-axis column.
        - y: str, optional
            The name of the y-axis column.

        This function uses Matplotlib to create a bar chart for the sum of values in the specified columns.

        """

        # Grouping and sorting the data
        grouped_data = self.df.groupby(x)[y].sum().nlargest(10).sort_values(ascending=False)

        # Plotting with Matplotlib
        fig, ax = plt.subplots(figsize=(12, 7))
        bars = ax.bar(grouped_data.index, grouped_data.values)

        # Adding labels to the bars
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

        ax.set_title(f'Sum of {y.capitalize()} for Top 10 {x.capitalize()} (Matplotlib)')
        ax.set_xlabel(x.capitalize())
        ax.set_ylabel(f'Sum of {y.capitalize()}')

        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()