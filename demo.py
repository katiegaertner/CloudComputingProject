import dash
from dash import Dash, dcc, html
from google.cloud import bigquery
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__)
server = app.server

#constructing bigquery client object
client = bigquery.Client()

query = """
    SELECT 
        time_series_timestamp AS Date, 
        time_series_data AS Historical_and_Forecast, 
        prediction_interval_upper_bound AS Forecast_Upper_Bound, 
        prediction_interval_lower_bound AS Forecast_Lower_Bound
    FROM
    ML.EXPLAIN_FORECAST(MODEL chicago_crimes.mvt_monthly,
        STRUCT(30 AS horizon, 0.8 AS confidence_level))
    """

query1 = """
        SELECT ROUND(time_series_data) AS forecast 
        FROM `gaertnergcp.chicago_crimes.Daily_MVT_Forecast`
        WHERE time_series_timestamp = '2022-06-01 00:00:00 UTC'
        """

#API Request
query_job = client.query(query)
query_job_2 = client.query(query1)

#Query to Dataframe
df = query_job.to_dataframe()

res = query_job_2.result()
for row in res:
    output = "The daily thefts model forecasts " + str(row[0]) + " motor vehicle thefts in Chicago on June 1, 2022."

#Create Plot
fig = px.line(df, x='Date', y = df.columns[1:4], 
                title = 'Motor Vehicle Thefts in Chicago by Month from 2000 to 2024 (Historical and Forecasted)'
                )

fig.update_layout(yaxis={"title": "Total Monthly Thefts"}, legend={"title":""})

fig.update_layout(font_family="Times New Roman")

app.layout = html.Div(children = [
    html.H1("Motor Vehicle Thefts in Chicago"),
    html.Div(children = output),
    dcc.Graph(
        id = 'Motor Vehicle Thefts in Chicago from 2000 to 2022',
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8080)


#from flask import Flask
#from flask_restful import Api
#from google.cloud import bigquery

#app = Flask(__name__)
#api = Api(app)

#client = bigquery.Client()

#query = """
#        SELECT ROUND(time_series_data) AS forecast 
#        FROM `gaertnergcp.chicago_crimes.Daily_MVT_Forecast`
#        WHERE time_series_timestamp = '2022-06-01 00:00:00 UTC'
#        """

#query_job = client.query(query)

#@app.route('/', methods=['GET'])
#def demo():
    # Handle query_job result and return to flask to display
#    res = query_job.result()
#    for row in res:
#        output = "Forecast for Motor Vehicle Thefts in Chicago on June 1, 2022: " + str(row[0])
#        return output

#if __name__ == "__main__":
#    app.run(port=8080)