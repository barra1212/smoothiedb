import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)


app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


# VARIABLES
smoothie_recipes=mongo.db.smoothie_recipes
categories=mongo.db.categories


# HOME ROOT
@app.route('/')
@app.route('/get_smoothies')
def get_smoothies():
    return render_template("smoothies.html", smoothie_recipes=smoothie_recipes.find())
   

# ADD SMOOTHIE FUNCTION, LOAD EXISTING CATEGORIES
@app.route('/add_smoothie')
def add_smoothie():
    return render_template('addsmoothie.html',
    categories=categories.find())
    

# GO TO EDIT SMOOTHIE RECIPE PAGE
@app.route('/edit_smoothie/<smoothie_recipes_id>')
def edit_smoothie(smoothie_recipes_id):
    the_smoothie = mongo.db.smoothie_recipes.find_one({"_id": ObjectId(smoothie_recipes_id)})
    all_categories = categories.find()
    return render_template('edit_smoothie.html', smoothie=the_smoothie, categories=all_categories)


# UPDATE SMOOTHIE RECIPE AND WRITE TO THE DATABASE
@app.route('/update_smoothie/<smoothie_recipes_id>', methods=['POST'])
def update_smoothie(smoothie_recipes_id):
    smoothie_recipes=mongo.db.smoothie_recipes
    ingredients = request.form.get('ingredients')
    ingredient_list = ingredients.splitlines()
    keyword_search = request.form.get('keyword_search').lower()
    keyword_search_list = keyword_search.splitlines()
    smoothie_recipes.update( {'_id': ObjectId(smoothie_recipes_id)},
    {
        "smoothie_name": request.form.get('smoothie_name'),
        "category_name": request.form.get('category_name'),
        "description": request.form.get('description'),
        "ingredients": ingredient_list,
        "method": request.form.get('method'),
        "calories": request.form.get('calories'),
        "keyword_search": keyword_search_list,
        "upvotes": int(0),
    })
    return redirect(url_for('get_smoothies'))


# WRITE NEW SMOOTHIE RECIPE TO THE DATABASE
@app.route('/insert_smoothie', methods=['POST'])
def insert_smoothie():
    ingredients = request.form.get('ingredients')
    ingredient_list = ingredients.splitlines()
    keyword_search = request.form.get('keyword_search').lower()
    keyword_search_list = keyword_search.splitlines()
    smoothie = {
        "smoothie_name": request.form.get('smoothie_name'),
        "category_name": request.form.get('category_name'),
        "description": request.form.get('description'),
        "ingredients": ingredient_list,
        "method": request.form.get('method'),
        "calories": request.form.get('calories'),
        "keyword_search": keyword_search_list,
        "upvotes": int(0),
    }
    smoothie_recipes.insert_one(smoothie)
    return redirect(url_for('get_smoothies'))


# DELETE SMOOTHIE
@app.route('/delete_smoothie/<smoothie_recipes_id>')
def delete_smoothie(smoothie_recipes_id):
    smoothie_recipes.remove({'_id': ObjectId(smoothie_recipes_id)})
    return redirect(url_for('get_smoothies'))


# VIEW EXISTING CATEGORIES
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=categories.find())


# ADD CATEGORY PAGE
@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


# WRITE NEW CATEGORY TO THE DATABASE
@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name').lower()}
    categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


# DELETE A CATEGORY
@app.route('/delete_category/<category_id>', methods=['POST'])
def delete_category(category_id):
    categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


# EDIT A CATEGORY (UNUSED)
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=categories.find_one({'_id': ObjectId(category_id)}))


# UPDATE A CATEGORY (UNUSED)
@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


# UPVOTE A SMOOTHIE RECIPE
# CREDIT TO SHANE MUIRHEAD ON SLACK FOR UPVOTE HELP
@app.route('/upvote/<smoothie_recipes_id>')
def upvote(smoothie_recipes_id):
    smoothie_recipes.find_one_and_update(
        {'_id': ObjectId(smoothie_recipes_id)},
        {'$inc': {'upvotes': int(1)}}
    )
    return redirect(url_for('get_smoothies')) 


# SEARCH FUNCTION BASED ON KEYWORDS IN RECIPE
@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('keyword_search')
    result = smoothie_recipes.find({"keyword_search" : search_term.lower()})
    return render_template("search-results.html", result=result)
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)