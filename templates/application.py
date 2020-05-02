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
    return render_template("success.html")


    