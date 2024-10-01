# TT_Sprint4_vehicles
This is a repository for TT Sprint 4 Project analyzing car advertisement data. It creates a web application on Render to expore the data through visual graphs for random events, i.e., used vehicle sales. Specifically, the graphs look at overall vehicle sales and certain factors (e.g., condition, model year, color) as they compare to price and days listed/days advertised.

The live interactive application for this project on Render is here:
https://tt-sprint-4-vehicles.onrender.com/

This project uses car advertisement data from the US (vehicles_us.csv) available here: https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv

To run the program, Python 3 (3.11.5) was used with the following packages: pandas, streamlit, plotly.express.

The virtual environment contained the following versions which were used for the requirements file when deploying to Render:
pandas==2.1.4
streamlit==1.29.0
plotly.express==0.4.1
altair==5.2.0

To launch this project on a local machine, the data set should be accessible in the project folder along with the app.py file, and python lanched with the above listed packages installed. The app.py file contains the code to launch locally or to use with a Render account. From Terminal/command prompt when in the folder where the data set and app.py is listed, use: streamlit run app.py. Once launched, the URL to view the app locally will be listed in the Terminal/command prompt.
