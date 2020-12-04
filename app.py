#!/usr/bin/env python
# coding: utf-8
import streamlit as st
st.write('''
# MA 346 Final Project 
## Cassidy Gorsky & Vivian Xia
''')

st.write('''
Our data is based on various information related to movies in 2017, 2018, 2019, and 2020. 
Our data source, https://www.the-numbers.com/, contains various information on movies from different years. 
Our main goal is to see how the pandemic impacted the movie industry by comparing different measurements of all the years.
''')

st.write('''
Here is the link to our GitHub repository: https://github.com/vivian-xia/MA346_Final_Project 
''')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from urllib.request import Request, urlopen #from stack overflow
from lxml import html

def import_table(year,table_title):
    req = Request('https://www.the-numbers.com/market/'+year+'/'+table_title, #ask a server on the internet to get data info
                headers={'User-Agent': 'Mozilla/5.0'}) #had to change browser to be "Firefox"
    webpage = urlopen(req).read()
    return pd.read_html(webpage) #get all the tables you can from this html in the form of dataframes

df_2019_top_movies = import_table('2019','top-grossing-movies')[0]
df_2020_top_movies = import_table('2020','top-grossing-movies')[0]
df_2019_distributor = import_table('2019','distributors')[1]
df_2020_distributor = import_table('2020','distributors')[1]

df_2017_top_movies = import_table('2017','top-grossing-movies')[0]
df_2018_top_movies = import_table('2018','top-grossing-movies')[0]
df_2017_distributor = import_table('2017','distributors')[1]
df_2018_distributor = import_table('2018','distributors')[1]

df_2019_top_movies.drop(df_2019_top_movies.tail(2).index, inplace = True)
df_2020_top_movies.drop(df_2020_top_movies.tail(2).index, inplace = True)
df_2017_top_movies.drop(df_2017_top_movies.tail(2).index, inplace = True)
df_2018_top_movies.drop(df_2018_top_movies.tail(2).index, inplace = True)


df_2019_distributor['2019 Gross'] = df_2019_distributor['2019 Gross'].str.replace('$','').str.replace(',','').astype(float)
df_2020_distributor['2020 Gross'] = df_2020_distributor['2020 Gross'].str.replace('$','').str.replace(',','').astype(float)

df_2019_top_movies['2019 Gross'] = df_2019_top_movies['2019 Gross'].str.replace('$','').str.replace(',','').astype(float)
df_2020_top_movies['2020 Gross'] = df_2020_top_movies['2020 Gross'].str.replace('$','').str.replace(',','').astype(float)

df_2017_distributor['2017 Gross'] = df_2017_distributor['2017 Gross'].str.replace('$','').str.replace(',','').astype(float)
df_2018_distributor['2018 Gross'] = df_2018_distributor['2018 Gross'].str.replace('$','').str.replace(',','').astype(float)

df_2017_top_movies['2017 Gross'] = df_2017_top_movies['2017 Gross'].str.replace('$','').str.replace(',','').astype(float)
df_2018_top_movies['2018 Gross'] = df_2018_top_movies['2018 Gross'].str.replace('$','').str.replace(',','').astype(float)


df_2019_distributor['2019 Gross/Movies'] = df_2019_distributor['2019 Gross'] / df_2019_distributor['Movies']
df_2019_distributor['2019 Gross/Movies'] = df_2019_distributor['2019 Gross/Movies'].astype(float)

df_2020_distributor['2020 Gross/Movies'] = df_2020_distributor['2020 Gross'] / df_2020_distributor['Movies']
df_2020_distributor['2020 Gross/Movies'] = df_2020_distributor['2020 Gross/Movies'].astype(float)

df_2017_distributor['2017 Gross/Movies'] = df_2017_distributor['2017 Gross'] / df_2017_distributor['Movies']
df_2017_distributor['2017 Gross/Movies'] = df_2017_distributor['2017 Gross/Movies'].astype(float)

df_2018_distributor['2018 Gross/Movies'] = df_2018_distributor['2018 Gross'] / df_2018_distributor['Movies']
df_2018_distributor['2018 Gross/Movies'] = df_2018_distributor['2018 Gross/Movies'].astype(float)


dist_2017 = df_2017_top_movies.groupby('Distributor')['2017 Gross'].max()
dist_2017_max = pd.DataFrame(dist_2017)
dist_2017_max.reset_index(inplace=True)
dist_2017_max = dist_2017_max.rename(columns = {'index': 'Distributor','2017 Gross':'2017 Gross Max'})
df_dist_2017 = pd.merge(dist_2017_max, df_2017_distributor, on= 'Distributor')
df_dist_2017 = df_dist_2017[['Distributor','2017 Gross Max', '2017 Gross/Movies']]

dist_2018 = df_2018_top_movies.groupby('Distributor')['2018 Gross'].max()
dist_2018_max = pd.DataFrame(dist_2018)
dist_2018_max.reset_index(inplace=True)
dist_2018_max = dist_2018_max.rename(columns = {'index': 'Distributor','2018 Gross':'2018 Gross Max'})
df_dist_2018 = pd.merge(dist_2018_max, df_2018_distributor, on= 'Distributor')
df_dist_2018 = df_dist_2018[['Distributor','2018 Gross Max', '2018 Gross/Movies']]

dist_2019 = df_2019_top_movies.groupby('Distributor')['2019 Gross'].max()
dist_2019_max = pd.DataFrame(dist_2019)
dist_2019_max.reset_index(inplace=True)
dist_2019_max = dist_2019_max.rename(columns = {'index': 'Distributor','2019 Gross':'2019 Gross Max'})
df_dist_2019 = pd.merge(dist_2019_max, df_2019_distributor, on= 'Distributor')
df_dist_2019 = df_dist_2019[['Distributor','2019 Gross Max', '2019 Gross/Movies']]

dist_2020 = df_2020_top_movies.groupby('Distributor')['2020 Gross'].max()
dist_2020_max = pd.DataFrame(dist_2020)
dist_2020_max.reset_index(inplace=True)
dist_2020_max = dist_2020_max.rename(columns = {'index': 'Distributor','2020 Gross':'2020 Gross Max'})
df_dist_2020 = pd.merge(dist_2020_max, df_2020_distributor, on= 'Distributor')
df_dist_2020 = df_dist_2020[['Distributor','2020 Gross Max', '2020 Gross/Movies']]


df_merge_gross= pd.merge(df_dist_2020, df_dist_2019, on = 'Distributor', how = 'right' )
df_merge_gross['2020 Gross Max'] = df_merge_gross['2020 Gross Max'].replace(np.nan,0)
df_merge_gross['2020 Gross/Movies'] = df_merge_gross['2020 Gross/Movies'].replace(np.nan,0)

df_merge_gross2020= pd.merge(df_dist_2020, df_dist_2017, on = 'Distributor', how = 'right' )
df_merge_gross2020['2020 Gross Max'] = df_merge_gross2020['2020 Gross Max'].replace(np.nan,0)
df_merge_gross2020['2020 Gross/Movies'] = df_merge_gross2020['2020 Gross/Movies'].replace(np.nan,0)

df_merge_gross2019= pd.merge(df_dist_2019, df_dist_2017, on = 'Distributor', how = 'right' )
df_merge_gross2019['2019 Gross Max'] = df_merge_gross2019['2019 Gross Max'].replace(np.nan,0)
df_merge_gross2019['2019 Gross/Movies'] = df_merge_gross2019['2019 Gross/Movies'].replace(np.nan,0)

df_merge_gross2018= pd.merge(df_dist_2017, df_dist_2018, on = 'Distributor', how = 'right' )
df_merge_gross2018['2017 Gross Max'] = df_merge_gross2018['2017 Gross Max'].replace(np.nan,0)
df_merge_gross2018['2017 Gross/Movies'] = df_merge_gross2018['2017 Gross/Movies'].replace(np.nan,0)

st.write("We are looking for the relationship between how "
         "much a distributor made per movie in 2017 and a chosen year by creating a scatter plot.")

st.sidebar.header("Comparing 2017 data to a year in a scatter plot")
yrscatter = st.sidebar.selectbox("Pick a Year",(2018,2019,2020))

if yrscatter == 2018:
    scatter = sns.lmplot( x='2017 Gross/Movies',y='2018 Gross/Movies', data=df_merge_gross2018)
    plt.ylim(0,80000000)
    plt.xlim(0,80000000)
    plt.title("2017 Gross/Movies vs. 2018 Gross/Movies Plot")
    st.pyplot(plt.gcf(),True)
elif yrscatter == 2019:
    scatter = sns.lmplot( x='2017 Gross/Movies',y='2019 Gross/Movies', data=df_merge_gross2019)
    plt.ylim(0,80000000)
    plt.xlim(0,80000000)
    plt.title("2017 Gross/Movies vs. 2019 Gross/Movies Plot")
    st.pyplot(plt.gcf(),True)
else:
    scatter = sns.lmplot( x='2017 Gross/Movies',y='2020 Gross/Movies', data=df_merge_gross2020)
    plt.ylim(0,80000000)
    plt.xlim(0,80000000)
    plt.title("2017 Gross/Movies vs. 2020 Gross/Movies Plot")
    st.pyplot(plt.gcf(),True)

st.write("Looking at the trend line when 2020 and 2017, we can see that the slope is considerably less steep compared to 2018 and 2019."
         "This means that the movie distributors generally made more money "
         "per movie in 2018 and 2019 compared to 2020. ")

st.sidebar.header("Comparing Two Genres in a bar plot")
genre_list = df_2019_top_movies['Genre'].unique().tolist()
genre1 = st.sidebar.selectbox("Pick a first genre",(genre_list))
genre2 = st.sidebar.selectbox("Pick a second genre",(genre_list))

st.header("Exploring Ticket Sales by Genre")
st.write("You can pick two genres in the sidebar to compare the average ticket sales between the four years."
         "The data will be represented as a bar plot.")

genre_2020 = df_2020_top_movies.groupby('Genre')['Tickets Sold'].mean()
genre_2019 = df_2019_top_movies.groupby('Genre')['Tickets Sold'].mean()
genre_2018 = df_2018_top_movies.groupby('Genre')['Tickets Sold'].mean()
genre_2017 = df_2017_top_movies.groupby('Genre')['Tickets Sold'].mean()
g20 = round(genre_2020[genre1])
g19 = round(genre_2019[genre1])
g18 = round(genre_2018[genre1])
g17 = round(genre_2017[genre1])
g220 = round(genre_2020[genre2])
g219 = round(genre_2019[genre2])
g218 = round(genre_2018[genre2])
g217 = round(genre_2017[genre2])
list1 = [g17,g18,g19,g20,g217,g218,g219,g220]

d = {'Year':[2017,2018,2019,2020,2017,2018,2019,2020] , 'Avg Tickets': list1, 'Genre':[genre1,genre1,genre1,genre1,genre2,genre2,genre2,genre2]}
df = pd.DataFrame(data= d)
g = sns.set_style("darkgrid")
g = sns.catplot(
    data=df, kind="bar",
    x="Year", y="Avg Tickets", hue="Genre",
    ci="sd", palette="bright", alpha=.6, height=6, legend= True
)
g.fig.suptitle(f"Comparing Genres {genre1} and {genre2}")
st.pyplot(plt.gcf(),True)
st.write("As you can see, the ticket sales from 2020 for each genre are always the lowest."
         "The pandemic has had a big impact on tickets sold since theatres had to shut down.")

st.header("Exploring Heatmaps")
st.write("This is a heat map containing 2017 Gross/Movies, 2018 Gross/Movies, 2017 Gross Max, and "
         "2018 Gross Max.This will allow us to see the correlations between "
         "the variables.")

df_heat_map = df_merge_gross2018.iloc[:,[1,2,3,4]]
correlation_coefficients = np.corrcoef( df_heat_map, rowvar=False )
labels = df_heat_map.columns
heatmap = sns.heatmap(correlation_coefficients, xticklabels = labels, yticklabels = labels, annot=True)
st.pyplot(plt.gcf(), True)

st.write("This is a heat map containing 2019 Gross/Movies, 2020 Gross/Movies, 2019 Gross Max, and "
         "2020 Gross Max.This will allow us to see the correlations between "
         "the variables.")
df_heat_map = df_merge_gross[['2019 Gross/Movies','2020 Gross/Movies','2019 Gross Max', '2020 Gross Max']]
correlation_coefficients = np.corrcoef( df_heat_map, rowvar=False )
labels = df_heat_map.columns
heatmap = sns.heatmap(correlation_coefficients, xticklabels = labels, yticklabels = labels, annot=True)
st.pyplot(plt.gcf(), True)

st.write("Between 2020 Gross/Movies and  2019 Gross/Movies, there is a correlation of 0.60. "
         "This is a weak positive correlation. "
         "This weak correlation means the the money made per movie in 2019 has a small effect on "
         "how much money per movie the distributor will make in 2020."
         "On the other hand, 2017 Gross/Movies and 2018 Gross/Movies have a correlations of 0.95."
         "This is a strong positive correlation that represents the money made per movie in 2017 had a significant impact on "
         "how much money per movie the distributor made in 2018.")

st.header("Distribution of Tickets Sold")
st.write("We explored a histogram that compared the tickets sold for 2019 and 2020. "
         "You are able to change the bin number on the slider below.")

n = st.slider("Bin number",4,20,10,2)
bins = np.linspace(0,10000000,n)
plt.hist([ df_2019_top_movies['Tickets Sold'],df_2020_top_movies['Tickets Sold']], bins= bins,label=['2019','2020'] )
plt.xlabel( 'Tickets Sold' )
plt.ylabel( 'Frequency' )
plt.title( 'Distribution of Tickets Sold' )
plt.legend()
st.pyplot(plt.gcf(), True)

st.write("There is a significant difference between the number of tickets sold in 2019 versus 2020."
         "The frequency of ticket purchases in 2019 for each bin is evidently larger than in 2020. "
         "For zero to one million ticket sold, 2019 tickets sold more than 500 times "
         "versus that of 2020 tickets sold a little more than 300 times.")
