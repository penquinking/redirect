from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("http://127.0.0.1:80")