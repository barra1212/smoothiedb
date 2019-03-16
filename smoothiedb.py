import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_smoothies')
def get_smoothies():
    return render_template("smoothies.html", smoothie_recipes=mongo.db.smoothie_recipes.find())
   

@app.route('/add_smoothie')
def add_smoothie():
    return render_template('addsmoothie.html')
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)