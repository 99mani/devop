from flask import Flask

# create flask app
app = Flask(__name__)


# add all the routes

@app.route("/", methods=["GET"])
def root():
    return "welcome to ITIL EXAM"

@app.route("/module", methods=["GET"])
def roote():
    return "DITISS ITIL Devops"

@app.route("/me", methods=["GET"])
def rotee():
    return "prn =23344223026 manisha 98984433"


# run the application
app.run(host="0.0.0.0", port=4000, debug=True)
