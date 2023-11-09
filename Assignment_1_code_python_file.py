# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 02:21:30 2023

@author: RUCHITABEN
"""

import pandas as pd
import matplotlib.pyplot as plt


def linechartfunction():
    df = pd.read_csv(
        'C:/Users/HP/OneDrive/Desktop/Assignment_1/population.csv')

    data_select_column = df.loc[0:4, ['Country Name', '2014 [YR2014]', 
    '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]', '2018 [YR2018]', 
    '2019 [YR2019]']]
    # Transpose
    df_t = pd.DataFrame.transpose(data_select_column)
    # first line containing country names into the header
    df_t.columns = df_t.iloc[0]
    # remove the first two lines (not containing numerical data)
    df_t = df_t[2:]
    # clean data drop na
    df_clean = df_t[["India", "Afghanistan",
                     "Costa Rica", "Somalia", "China"]].dropna()
    plt.figure()
    plt.plot(df_clean.index, df_clean["India"], label="India")
    plt.plot(df_clean.index, df_clean["Afghanistan"], label="Afghanistan")
    plt.plot(df_clean.index, df_clean["Costa Rica"], label="Costa Rica")
    plt.plot(df_clean.index, df_clean["Somalia"], label="Somalia")
    plt.plot(df_clean.index, df_clean["China"], label="China")
    plt.legend()
    plt.savefig("C:/Users/HP/OneDrive/Desktop/Assignment_1/linegraph_1.png")


def piechartfunction():
    # DataFrame of each student and the votes they get
    dataframe_country_population = pd.DataFrame({'Country Name': ['India', 
    'Afghanistan', 'Costa Rica', 'Somalia', 'China'],
    'population_in_2014': [1.307247e+09, 3.271621e+07, 4.844288e+06,
    1.330924e+07, 1.371860e+09]})
    # Plotting the pie chart for above dataframe
    dataframe_country_population.groupby(['Country Name']).sum().plot(
        kind='pie', y='population_in_2014')
    # Plotting the pie chart for above dataframe
    dataframe_country_population.groupby(['Country Name']).sum().plot(
    kind='pie', y='population_in_2014', autopct='%1.0f%%')
    colors = ['black', 'steelblue', 'orange', 'yellow', 'red']
    # Plotting the pie chart for above dataframe
    dataframe_country_population.groupby(['Country Name']).sum().plot(
    kind='pie', y='population_in_2014',
    autopct='%1.0f%%', colors=colors)
    plt.savefig("C:/Users/HP/OneDrive/Desktop/Assignment_1/myplot.png")


def barchartfunction():
    data_plot_bar = pd.read_csv(
    'C:/Users/HP/OneDrive/Desktop/Assignment_1/mortality_rate.csv', 
    skiprows=[0, 1, 2])
    data_select_column_bar = data_plot_bar.loc[0:4, ['Country Name', '2021']]
    data_select_column_bar.plot(x='Country Name', y='2021', kind='bar')
    plt.xlabel('Country Name')
    plt.ylabel('Values')
    plt.title('Bar Chart Example')
    plt.xticks(rotation=90)  # Rotate x-axis labels if needed
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines
    plt.tight_layout()  # Ensure everything fits in the plot
    plt.savefig("C:/Users/HP/OneDrive/Desktop/Assignment_1/myplot.png")

#Calling Funtions
linechartfunction()
piechartfunction()
barchartfunction()

#Show the graph
plt.show()
