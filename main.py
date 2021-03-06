from flask import Flask
from flask_restful import Api
from google.cloud import bigquery

app = Flask(__name__)
api = Api(app)

client = bigquery.Client()

query = """
        SELECT ROUND(time_series_data) AS forecast 
        FROM `gaertnergcp.chicago_crimes.Daily_MVT_Forecast`
        WHERE time_series_timestamp = '2022-06-01 00:00:00 UTC'
        """

query_job = client.query(query)

df = query_job.to_dataframe()
json_object = df.to_json(orient='records')

@app.route('/', methods=['GET'])
def main():
    response = json_object
    return response


