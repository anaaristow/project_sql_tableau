import pandas as pd
import numpy as np

def group_df_guns_sold_per_year(dataframe):

    '''Groups the DataFrame of Firearm Sales by year and state, summing the totals.'''
    
    dataframe['data'] = pd.to_datetime(dataframe['data'], format='%d/%m/%Y')
    dataframe['year'] = dataframe['data'].dt.year
    grouped_sold = dataframe.groupby(['year', 'state']).agg({'totals': 'sum'}).reset_index()
    return grouped_sold
    
def group_df_incidents_per_year(dataframe):

    ''' Groups the DataFrame of Gun Violence incidents by year and state,
    summing the number of injured and killed.'''

    dataframe['date'] = pd.to_datetime(dataframe['date'], format='%d/%m/%Y')
    dataframe['year'] = dataframe['date'].dt.year
    grouped_incidents = dataframe.groupby(['year', 'state']).agg({'n_injured': 'sum', 'n_killed': 'sum'}).reset_index()
    return grouped_incidents

