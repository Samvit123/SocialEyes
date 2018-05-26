import os, app
from flask import Flask, render_template, request
flaskapp = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/ubuntu/socialeyes/SocialEye-c146dba1d667.json"

@flaskapp.route("/")
def index():
  return render_template("index.html")

@flaskapp.route("/submitHandle", methods=['POST'])
def submitHandle():
  return (request.form['twitterHandle'])

@flaskapp.route("/stats")
def stats():
  app.classify()
  return render_template("stats.html")


if __name__ == '__main__':
  flaskapp.run(host="0.0.0.0", port="8080")
