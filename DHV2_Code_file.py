# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:09:44 2023

@author: RUCHITABEN SHAILESHBHAI KABARIYA
"""

import pandas as pd
import matplotlib.pyplot as plt


def read_csv(csv_file_name):
    """


    Parameters
    ----------
    csv_file_name : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    countries = ["India", "Australia", "China", "Philippines", "Brazil"]
    col_filter = ["2000", "2005", "2010", "2015", "2020"]

    year_data = pd.read_csv(csv_file_name, skiprows=3, iterator=False)

    year_data.index = year_data["Country Name"]
    year_data = year_data.loc[countries, col_filter]
    year_data.columns = year_data.columns.astype(int)
    year_data.dropna(axis=1)
    country_data = year_data.T
    return country_data, year_data


def show_stat(df_stat, title):
    print("======", title)
    print("--describe")
    print(df_stat.describe())
    print("--median")
    print(df_stat.median())
    print("--skew")
    print(df_stat.skew())
    print("--kurtosis")
    print(df_stat.kurtosis())


def plot_corr(country, df_electricity_acess_rural, df_electricity_acess_urban, df_elecOil, df_elecCoal):
    df_corr = pd.DataFrame()
    df_corr["electricity acess rural"] = df_electricity_acess_rural[country].values
    df_corr["electricity acess urban"] = df_electricity_acess_urban[country].values
    df_corr["electricity_oil"] = df_elecOil[country].values
    df_corr["electricity_coal"] = df_elecCoal[country].values
    corr_mat = df_corr.corr()
    plt.figure()
    plt.imshow(corr_mat, cmap="Blues")
    plt.xticks(range(len(corr_mat)), corr_mat.columns, rotation=90)
    plt.yticks(range(len(corr_mat)), corr_mat.columns)

    plt.colorbar()
    plt.title(country)
    plt.savefig(country+".png", dpi=300)


def plot_line_chart(title, xlbl, ylbl, df):
    plt.figure(figsize=(10, 6))
    ap = df.plot(title=title)
    ap.set_ylabel(ylbl)
    ap.set_xlabel(ylbl)
    fig = ap.get_figure()
    fig.savefig(title+".png")


def plot_bar_chart(title, xlbl, ylbl, df):
    """


    Parameters
    ----------
    title : TYPE
        DESCRIPTION.
    xlbl : TYPE
        DESCRIPTION.
    ylbl : TYPE
        DESCRIPTION.
    df : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    plt.figure(figsize=(10, 6))
    ap = df.plot.bar(title=title)
    ap.set_ylabel(ylbl)
    ap.set_xlabel(ylbl)
    fig = ap.get_figure()
    fig.savefig(title+".png")


# country_forst_land,year_forest_land = read_csv("API_AG.LND.FRST.K2_DS2_en_csv_v2_5995336.csv")
country_name_electricity_acess_rural, year_name_electricity_acess_rural = read_csv(
    "API_EG.ELC.ACCS.RU.ZS_DS2_en_csv_v2_6228450.csv")
country_name_electricity_acess_urban, year_name_electricity_acess_urban = read_csv(
    "API_EG.ELC.ACCS.UR.ZS_DS2_en_csv_v2_6228451.csv")
country_electricity_oil, year_electricity_oil = read_csv(
    "API_EG.ELC.PETR.ZS_DS2_en_csv_v2_6234678.csv")
country_electricity_coal, year_electricity_coal = read_csv(
    "API_EG.ELC.COAL.ZS_DS2_en_csv_v2_6228498.csv")

show_stat(country_name_electricity_acess_rural, "Electricity Rural")

plot_bar_chart("Access of electricity rural title", "years",
               "Access of electricity rural", year_name_electricity_acess_rural)
plot_bar_chart("Access of electricity urban title", "years",
               "Access of electricity urban", year_name_electricity_acess_urban)
plot_line_chart("electricity_acess_rural title", "years",
                "electricity_acess_rural", country_name_electricity_acess_rural)
plot_line_chart("electricity_acess_urban title", "years",
                "electricity_acess_urban", country_name_electricity_acess_urban)


plot_corr("India", country_name_electricity_acess_rural, country_name_electricity_acess_urban,
          country_electricity_oil, country_electricity_coal)

plt.show()
