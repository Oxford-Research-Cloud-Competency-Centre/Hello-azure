from flask import Flask, render_template

app = Flask(__name__, template_folder=".")

@app.route("/")
def home():
    return render_template("index.html")
	
@app.route("/hello_api")
def hello_api():
    return {
		"name": "Wrinkle Five Star",
		"species": "Duck",
		"breed": "American Pekin",
		"hatching_date": "2020-09-09",
		"sex": "Male"
    }