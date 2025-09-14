from pydoc import render_doc
from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return render_doc("form.html")