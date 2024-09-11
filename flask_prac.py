import pandas
import flask

app = flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return '<h1>Home<h1>'

@app.route('/application',methods=['GET'])
def applications():
    return {'application_status': 'OPEN'}