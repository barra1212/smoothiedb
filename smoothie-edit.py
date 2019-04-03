# GO TO EDIT SMOOTHIE RECIPE PAGE
@app.route('/edit_smoothie/<smoothie_recipe_id>')
def edit_smoothie(smoothie_recipe_id):
    the_smoothie = smoothie_recipes.find_one({"_id": ObjectId(smoothie_recipe_id)})
    all_categories =  categories.find()
    return render_template('edit_smoothie.html', smoothie=the_smoothie, categories=all_categories)
    
    
# UPDATE SMOOTHIE RECIPE AND WRITE TO THE DATABASE
@app.route('/update_smoothie/<smoothie_recipe_id>', methods=['POST'])
def update_smoothie(smoothie_recipe_id):
    smoothie_recipes=mongo.db.smoothie_recipes
    ingredients = request.form.get('ingredients')
    ingredient_list = ingredients.splitlines()
    keyword_search = request.form.get('keyword_search')
    keyword_search_list = keyword_search.splitlines()
    smoothie_recipes.update( {'_id': ObjectId(smoothie_recipe_id)},
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
