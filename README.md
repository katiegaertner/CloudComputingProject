# Forecasting Motor Vehicle Theft Via Google Cloud Platform and Dash

This project was done for the Northwestern MS Data Science Analytics Application Engineering course. The project objective was to create a Machine Learning application deployed through a Continuous Integration and Continuous Development (CI/CD) pipeline hosted on Google Cloud Platform’s (GCP) App Engine.

I chose to use historical crime data for the city of Chicago to forecast motor vehicle thefts (MVT) in Chicago over various time intervals. The app outputs the forecasted number of MVTs in Chicago on a specific day (in this case, June 1, 2022) as well as a graph depicting historical MVTs at the monthly level, forecasted monthly MVTs with an upper and lower forecast bound at the 80% confidence level.

## Set Up

Files for the project were created and managed on a GCP project virtual environment. Files were then pushed to GitHub, where an automated GitHub workflow file built and deployed the project elements. The workflow was divided into two major tasks: (1) building the environment, which included linting and testing the application; and (2) deploying to Google App Engine using Google Credentials. The credentials were created using SSH keys from GCP and added to GitHub as “secrets.”

## Architecture

<img width="1020" alt="Cloud Project Architecture Map" src="https://user-images.githubusercontent.com/96923975/171256238-7da986f2-1dbb-46ee-ba1e-af2b05eb2a05.png">

## Application

I used GCP’s BigQuery to source the publicly-available Chicago Crimes dataset, and BigQuery ML to create an ARIMA_PLUS time series model to forecast Motor Vehicle Thefts in Chicago at monthly and daily levels. The resulting forecast and historical data were saved to a GCP table and pulled into the application using the BigQuery Client API. The June 1, 2022 forecast is produced from the daily model, and the graph depicting historical and forecasted thefts is produced from the monthly model. The information was pushed to the app using Dash in in the demo.py file, and can be accessed via https://gaertnergcp.uc.r.appspot.com/ as website with interactive hovering capability for the graphic.

## Result

When navigating to the active application URL, a user will see the following:

![Cloud Project App Outcome](https://user-images.githubusercontent.com/96923975/171253843-8047b327-15d6-4435-89c0-cd6ecfae59fd.png)

## Demonstration
