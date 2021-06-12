from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
# import fast_food.py
import fast_food

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/fastfood")

# Get the data to load to MongoDB through a function
data = fast_food.load_data()
#print(data)

# Update the Mongo database using update and upsert=True
#mongo.db.collection.update_many({}, data, upsert=True)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Return template and data
    return render_template("index.html")

# Route that will display the JSON
@app.route("/json/<state>") #variables in the route to get the specific data
def json(state):
    # Find the fast food data from the mongo database
    if (state == "ALL USA"):
        ff_data = list(mongo.db.collection.find())
    else:
        ff_data = list(mongo.db.collection.find({"state": state}))
    # Return the JSON data
    return dumps(ff_data)

if __name__ == "__main__":
    app.run(debug=True)
