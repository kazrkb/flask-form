
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email")
    password = request.form.get("password")
    
    # if email == "admin@gmail.com" and password=="123":
    #     return render_template("welcome.html", email=email)
    valid_users = {
        'admin@gmail.com':'123',
        'doctor@outlook.com':'456',
        'student@hotmail.com':'hot'
    }
    if email in valid_users and password==valid_users[email]:
        return render_template("welcome.html",email=email)
    else:
        return "Invalid credentials"