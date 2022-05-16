import flask
from google.cloud import bigquery

bigquery_client = bigquery.Client()

app = flask.Flask(__name__)
@app.route("/")
def main():
    # Define query_job and query object
    query_job = bigquery_client.query(
        """
        SELECT ROUND(time_series_data) AS forecast 
        FROM `gaertnergcp.chicago_crimes.Daily_MVT_Forecast`
        WHERE time_series_timestamp = '2022-06-01 00:00:00 UTC'
        """
    )
   
    # Handle query_job result and return to flask to display
    res = query_job.result()
    for row in res:
        output = "Forecast for Motor Vehicle Thefts in Chicago on June 1: " + str(row[0])
        return output

if __name__ == "__main__":
    app.run(port=8080)