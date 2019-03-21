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
    return render_template('addsmoothie.html',
    categories=mongo.db.categories.find())


@app.route('/test')
def test():
    return render_template('test.html',
    smoothie_recipes=mongo.db.smoothie_recipes.find())
    

@app.route('/insert_smoothie', methods=['POST'])
def insert_smoothie():
    smoothie_recipes = mongo.db.smoothie_recipes
    ingredients = request.form.get('ingredients')
    ingredient_list = ingredients.splitlines()
    keyword_search = request.form.get('keyword_search')
    keyword_search_list = keyword_search.splitlines()
    smoothie = {
        "smoothie_name": request.form.get('smoothie_name'),
        "category_name": request.form.get('category_name'),
        "description": request.form.get('description'),
        "ingredients": ingredient_list,
        "method": request.form.get('method'),
        "calories": request.form.get('calories'),
        "keyword_search": keyword_search_list,
    }
    smoothie_recipes.insert_one(smoothie)
    return redirect(url_for('get_smoothies'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())


@app.route('/delete_category/<category_id>', methods=['POST'])
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)