import streamlit as st
import pandas as pd
import plotly.express as px

veh_df = pd.read_csv('vehicles_us.csv')

st.header(':green[Vehicle advertisements and sales]')

#creating histograms with mileage, condition, type and year
st.header('Histogram of mileage vs condition')
fig_d = px.histogram(veh_df, x='odometer', color='condition', nbins=50)
st.write(fig_d)

st.header('Histogram of type vs model year')
fig_a = px.histogram(veh_df, x='type', color='model_year')
st.write(fig_a)

#creating histogram with a checkbox to filter for vehicles priced over $10K
st.header('Histogram of days listed vs condition')
mask_filter = veh_df['price'] > 12000
df_filtered = veh_df[mask_filter]
highprice = st.checkbox("Priced > $12,000 (avg selling price)")
if highprice:
    fig_e = px.histogram(df_filtered, x='days_listed', color='condition')
else:
    fig_e = px.histogram(veh_df, x='days_listed', color='condition')
st.write(fig_e)

#creating additional histograms and scatterplots for price, color, mileage and days listed
st.header('Histogram of price vs color')
fig_b = px.histogram(veh_df, x='price', color='paint_color', nbins=100)
st.write(fig_b)

st.header('Plot of mileage vs price')
fig_j = px.scatter(veh_df, x='odometer', y='price')
st.write(fig_j)

st.header('Plot of price vs days listed')
fig_f = px.scatter(veh_df, x='price', y='days_listed', color='condition')
st.write(fig_f)
