# -----------------------------------------------------------------------------     
# Purpose:  CS 122 Final Project - Group 12
#           Extract and analyze data from the "Police Deaths" data set
#           to answer questions and make conclusions about the data
#           Data set: https://github.com/fivethirtyeight/data/blob/master/police-deaths/clean_data.csv
#
# Author:   Michelle Lai
# Date:     April 22, 2018
# -----------------------------------------------------------------------------

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

def graph_year_count(df):
    """
    Create and save a bar graph representing the count of police deaths for each year
    The x-axis is year, y-axis is count
    :param df: (dataframe) holding the data to be graphed
    """
    # set the visual features of the graph
    sns.set(font_scale=1.5)
    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 8)
    plt.xticks(rotation=45)
    ax.set_title("Yearly Police Deaths")
    # create the graph of the data
    plot = sns.barplot("year", "count", data=df, palette="winter_d")
    # plt.show()
    # save the graph as an image
    fig.savefig("1_graph_year_count.png")
    
def graph_decade_count(df):
    """
    Create and save a bar graph representing the count of police deaths for each decade
    The x-axis is decade, y-axis is count
    :param df: (dataframe) holding the data to be graphed
    """
    # set the visual features of the graph
    sns.set(font_scale=2)
    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 10)
    ax.set_title("Decade Police Deaths")
    # create the graph of the data
    plot = sns.barplot("decade", "count", data=df, palette="winter_d")
    # plt.show()
    # save the graph as an image
    fig.savefig("1_graph_decade_count.png")

def decade(year):
    """
    Calculate the decade given the year
    :param year: (set) representing the year
    :return: an integer representing the 4-digit decade of the given year
    """
    # get the first 3 digits of the year
    partial = (year[0]//10).item()
    # add a 0 to the end, return as decade
    return partial * 10

def graph_year_state_count(df):
    """
    Create and save a bar graph representing the count of police deaths for each state
    considering only years 2001 and 2007
    The x-axis is state, y-axis is count, legend is year
    :param df: (dataframe) holding the data to be graphed
    """
    # set the visual features of the graph
    sns.set(font_scale=2)
    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 10)
    plt.xticks(rotation=45)
    ax.set_title("2001 and 2007 State Police Deaths")
    # create the graph of the data
    plot = sns.barplot("state", "count", data=df, palette="bone", hue='year')
    # plt.show()
    # save the graph as an image
    fig.savefig("1_graph_top_state_count.png")
    
def graph_year_cause_count(df):
    """
    Create and save a bar graph representing the count of police deaths for each cause
    considering only years 2001 and 2007
    The x-axis is cause shorthand, y-axis is count, legend is year
    :param df: (dataframe) holding the data to be graphed
    """
    # set the visual features of the graph
    sns.set(font_scale=1.5)
    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 12)
    plt.xticks(rotation=25)
    ax.set_title("2001 and 2007 Police Death Causes")
    # create the graph of the data
    plot = sns.barplot("cause_short", "count", data=df, palette="bone", hue='year')
    # plt.show()
    # save the graph as an image
    fig.savefig("1_graph_top_cause_count.png")

def graph_cause_count(df):
    """
    Create and save a bar graph representing the count of police deaths for each year
    considering only causes related to vehicles
    The x-axis is year, y-axis is count, legend is cause shorthand
    :param df: (dataframe) holding the data to be graphed
    """
    # set the visual features of the graph
    sns.set(font_scale=2)
    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 12)
    plt.xticks(rotation=45)
    ax.set_title("Yearly Vehicle Accident Police Deaths")
    # create the graph of the data
    plot = sns.barplot("year", "count", data=df, palette="winter_d", ci=None)
    # plt.show()
    # save the graph as an image
    fig.savefig("2_graph_cause_count.png")
    
def graph_count_comparison(df):
    """
    Create and save a combination violin and swarm graph 
    representing the distribution of police deaths for each vehicle cause
    The x-axis is cause shorthand, y-axis is count
    :param df: (dataframe) holding the data to be graphed
    """
    # set the visual features of the graph
    sns.set(font_scale=2)
    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 10)
    ax.set_title("Distribution of Vehicle Police Deaths")
    # create the two graphs of the data and overlap them
    plot1 = sns.violinplot(x='cause_short', y='count', data=df, inner=None, palette="winter_d")
    plot2 = sns.swarmplot(x='cause_short', y='count', data=df, palette="Wistia")
    # plt.show()
    # save the graph as an image
    fig.savefig("2_graph_count_comparison.png")
    
def graph_cause_count_each(df, label):
    """
    Create and save a bar graph representing the count of police deaths 
    of one cause for every year
    The x-axis is year, y-axis is count
    :param df: (dataframe) holding the data to be graphed
    :param label: (string) representing the cause to be graphed
    """
    # set the visual features of the graph
    sns.set(font_scale=1.5)
    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 8)
    plt.xticks(rotation=45)
    ax.set_title(label.capitalize() + " Police Death Causes")
    # create the graph of the data
    plot = sns.barplot("year", "count", data=df, palette="winter_d")
    # plt.show()
    # save the graph as an image with the correct cause naming
    name = "2_graph_cause_count_" + label + ".png"
    fig.savefig(name)

def occurance(row):
    """
    Calculate the occurance percentage for the highest counted cause for the row
    :param row: (set) representing the row
    :return: an integer representing the percentage that the highest counted cause occurs
    """
    # divide the row's highest counted cause by the row's total number of deaths
    percentage = row['max_count'] / row['all_count']
    percentage *= 100
    # round the percentage up so it's two digits
    return round(percentage)

def graph_max_cause(df):
    """
    Create and save a bar graph representing the each state's highest counted cause of death
    The x-axis is state, y-axis is highest count, legend is highest counted cause shorthand
    :param df: (dataframe) holding the data to be graphed
    """
    # set the visual features of the graph
    sns.set(font_scale=2)
    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 10)
    plt.xticks(rotation=20)
    ax.set_title("States' Max Police Death Causes >= 150")
    # create the graph of the data
    plot = sns.barplot("state", "max_count", data=df, palette="bone", hue='max_cause')
    # plt.show()
    # save the graph as an image
    fig.savefig("3_graph_max_cause.png")
    
def graph_percentage_cause(df):
    """
    Create and save a combination violin and swarm graph representing the
    distribution of police deaths for each states' highest percentage cause of death
    The x-axis is highest counted cause shorthand, y-axis is the state's highest percentage
    :param df: (dataframe) holding the data to be graphed
    """
    # set the visual features of the graph
    sns.set(font_scale=2)
    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 12)
    plt.xticks(rotation=10)
    ax.set_title("Distribution of States' Max Percentage Occurred Cause")
    # create the two graphs of the data and overlap them
    plot1 = sns.violinplot(x='max_cause', y='max_occurance', data=df, inner=None, palette="winter_d")
    plot2 = sns.swarmplot(x='max_cause', y='max_occurance', data=df, palette="Wistia")
    # plt.show()
    # save the graph as an image
    fig.savefig("3_graph_max_percentage_comparison.png")
    

# read csv file
df = pd.read_csv('data.csv')
# remove US, not a state
df = df.loc[~df['state'].isin([' US'])].reset_index()


#################
# QUESTION 1
#################

# group the data by year and get the # of police deaths per year
year_count = df.groupby('year').size().reset_index()
# only get years >= 1990
year_recent = year_count[year_count.year >= 1990]
year_recent.rename(columns = {0:'count'}, inplace = True)
# graph the count of deaths for all years >= 1990
graph_year_count(year_recent)

# create the decade column, calculated for each row by its year
year_recent['decade'] = year_recent[['year']].apply(decade,axis=1)
# for each decade, get the mean # of deaths
decade_recent = year_recent.groupby('decade').mean().reset_index()
# graph the count of deaths for each decade
graph_decade_count(decade_recent)

# get the top 2 years only, 2001 and 2007
year_top = df.loc[df['year'].isin([2001, 2007])].reset_index()
# get the count of deaths for each state for each of the two years
year_top_state = year_top.groupby(['state', 'year']).size().reset_index()
year_top_state.rename(columns = {0:'count'}, inplace = True)
# only plot those with state deaths greater than 5
year_top_state = year_top_state[year_top_state['count'] >= 5]
# graph the count of deaths for each state of the top 2 years
graph_year_state_count(year_top_state)

# get the count of deaths for each cause of death for each of the two years
year_top_cause = year_top_state = year_top.groupby(['cause_short', 'year']).size().reset_index()
year_top_cause.rename(columns = {0:'count'}, inplace = True)
# only plot causes that have deaths greater than 5
year_top_cause = year_top_cause[year_top_cause['count'] >= 5]
# graph the count of deaths for each cause of the top 2 years
graph_year_cause_count(year_top_cause)


#################
# QUESTION 2
#################

# vehicle accidents include automobile, motorcycle, and aircraft related accidents
vehicle_causes = ["Automobile accident", "Motorcycle accident", "Aircraft accident"]
# filter to only analyze police deaths related to vehicle accidents
cause_df = df.loc[df['cause_short'].isin(vehicle_causes)].reset_index()

# get the count of deaths for each year for each of the vehicle causes
cause_group = cause_df.groupby(['year', 'cause_short']).size()
cause_group = cause_group.reset_index()
cause_group.rename(columns = {0:'count'}, inplace = True)
# only consider years >= 1980
cause_group = cause_group[cause_group.year >= 1980]
# graph the count of deaths for vehicle causes for each year
graph_cause_count(cause_group)

# compare count range for each of the 3 causes
graph_count_comparison(cause_group)

# create an individual graph for each vehicle cause
for cause in vehicle_causes:
    cause_single = cause_group.loc[cause_group['cause_short']==cause].reset_index()
    # get current cause for the label of the graph
    cause_label = cause.lower().split(" ")[0]
    graph_cause_count_each(cause_single, cause_label)


#################
# QUESTION 3
#################

# get the number of accidents for each state for each cause
state_count = df.groupby(['state', 'cause_short']).size().reset_index()
state_count.rename(columns = {0:'count'}, inplace = True)

# get the max counted cause for each state
state_max = state_count.groupby(['state']).max().reset_index()
state_max.rename(columns = {'count':'max_count', 'cause_short':'max_cause'}, inplace = True)
# get the min counted cause for each state
state_min = state_count.groupby(['state']).min().reset_index()
state_min.rename(columns = {'count':'min_count', 'cause_short':'min_cause'}, inplace = True)
# get the total count for every cause for each state
state_all = df.groupby(['state']).size().reset_index()
state_all.rename(columns = {0:'all_count'}, inplace = True)
# combine into one df to have min and max counts and causes and all cause counts for each state
state_minmax = state_min
state_minmax['max_cause'] = state_max['max_cause']
state_minmax['max_count'] = state_max['max_count']
state_minmax['all_count'] = state_all['all_count']

# get the percentage occurance of the max counted cause for each state
state_minmax['max_occurance'] = state_minmax.apply(occurance,axis=1)

# graph the highest occurance cause's percentage for each cause of every state
graph_percentage_cause(state_minmax)

# table for min/max (least/most) cause of death for each state
print(state_minmax[['state', 'min_cause', 'min_count']])
print(state_minmax[['state', 'max_cause', 'max_cause']])

# for graph, only consider >= 150 deaths
state_minmax_filter = state_minmax[state_minmax['max_count'] >= 150]
state_minmax_filter
# graph states' highest counted cause of death, must be greater than 150 
graph_max_cause(state_minmax_filter)
