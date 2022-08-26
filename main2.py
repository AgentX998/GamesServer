from db import read_scores,read_scores_latest,read_scores_email
from flask import Flask,request
app = Flask(__name__)

@app.route("/scores", methods=['GET'])
def scores():
    return read_scores()
@app.route("/latest", methods=['GET'])
def latest():
    return read_scores_latest()
@app.route("/my_scores", methods=['GET','POST'])
def my_scores():
    value=request.json['email']
    return read_scores_email(value)
if __name__ == '__main__':
    app.run(host="54.242.116.71", port=8000, debug=True)