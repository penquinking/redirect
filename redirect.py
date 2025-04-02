from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("http://169.254.169.254/latest/meta-data/iam/")
