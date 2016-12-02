#!/usr/bin/python
import pandas as pd
import matplotlib
import sys

def plot_county_data(county):
    for line in open("ELECTION_ID"):
        year,id = (int(x) for x in line.split())
        file_name = str(year)+ ".csv"

        header = pd.read_csv(file_name, nrows = 1).dropna(axis = 1)
        d = header.iloc[0].to_dict()
        df = pd.read_csv(file_name, index_col = 0, thousands = ",", skiprows = [1])
        df.rename(inplace = True, columns = d)
        df.dropna(inplace = True, axis = 1)
        df["Year"] = year
        df = df[column_headers]
        hist_list.append(df)
    data = pd.concat(hist_list)
    data["Republican Share"] = data["Republican"]/ data["Total Votes Cast"]
    county_data = data[data.index == county]

    graph = county_data.plot(x="Year", y="Republican Share")
    graph.get_figure().savefig('accomack.png') ##Why not just use the county name?

column_headers = ["Democratic", "Republican", "Total Votes Cast", "Year"]
hist_list = []

county = input("Enter a county to plot: ")
plot_county_data(county)
