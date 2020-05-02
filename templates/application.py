import smtplib
from flask import Flask, render_template, request

# Configure app
app = Flask(__name__)

# Registered students
students = []


# controllers
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure")
    students.append(f"{name} from {dorm}")
    return redirect("/regisrants")
    # return render_template("success.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    dorm = request.form.get("dorm")
    if not name or not email or not dorm:
        return render_template("failure.httml")
    message = "You are registered!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.long("samanb@ns.net", os.getenv("PASSWORD"))
    server.sendmail("samanb@ns.net", email, message)
    return render_template("success.html")
    