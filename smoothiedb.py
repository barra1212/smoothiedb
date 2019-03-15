import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

# app.config["MONGO_DBNAME"] = 'smoothiedb'
# app.config["MONGO_URI"] = 'mongodb+srv://barra:barra00User@myfirstcluster-gjsrn.mongodb.net/smoothiedb?retryWrites=true'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_smoothies')
def get_smoothies():
    return render_template("smoothies.html", smoothie_recipes=mongo.db.smoothie_recipes.find())
   
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)