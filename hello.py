from flask import Flask
#from flask_restful import Api

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Maggie" 

#if __name__ == "__main__":
#    app.run(port=8080)