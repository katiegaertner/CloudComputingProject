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

@app.route('/', methods=['GET'])
def demo():
    # Handle query_job result and return to flask to display
    res = query_job.result()
    for row in res:
        output = "Forecast for Motor Vehicle Thefts in Chicago on June 1, 2022: " + str(row[0])
        return output

#if __name__ == "__main__":
#    app.run(port=8080)