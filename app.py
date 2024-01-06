import streamlit as st
import pandas as pd
import plotly.express as px

veh_df = pd.read_csv('~/Documents/Data Science/Projects/TT_Sprint_4/TT_Sprint4_vehicles/vehicles_us.csv')

#full path '~/Documents/Data Science/Projects/TT_Sprint_4/TT_Sprint4_vehicles/vehicles_us.csv'

print(veh_df.head())

st.header('Histogram of mileage vs condition')

fig_d = px.histogram(veh_df, x='odometer', color='condition', nbins=50)
st.write(fig_d)
