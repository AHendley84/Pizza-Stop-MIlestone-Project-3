import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Render home template
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# Render all recipes to user
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipe_repository.find())
    return render_template("all_recipes.html", recipes=recipes)


# Render user recipes to user
@app.route("/my_recipes")
def my_recipes():
    recipes = list(mongo.db.recipe_repository.find())
    return render_template("my_recipes.html", recipes=recipes)


# Search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipe_repository.find({"$text": {"$search": query}}))
    return render_template("all_recipes.html", recipes=recipes)


# Register for an account
@app.route("/register", methods=["GET", "post"])
def register():
    if request.method == "POST":
        # Check if the username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please try another")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration completed successfully!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Log an existing user in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check to see if the user already exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Display user from db
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # obtain the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    
    fav = []

    for obj in username["favorites"]:
        recipe = mongo.db.recipe_repository.find_one({"_id": obj})
        fav.append(recipe)


    if session["user"]:
        return render_template("profile.html", username=username, fav=fav)

    return redirect(url_for("login"))


# Log user out
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Submit a recipe to the db
@app.route("/submit_recipe", methods=["GET", "POST"])
def submit_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_category": request.form.get("recipe_category"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_prep_time": request.form.get("recipe_prep_time"),
            "recipe_cook_time": request.form.get("recipe_cook_time"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_submitted_by": session["user"]
        }
        mongo.db.recipe_repository.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("submit_recipe.html", categories=categories)


# View a specific recipe in full from the db
@app.route("/view_recipe/<recipe_repository_id>")
def view_recipe(recipe_repository_id):
    recipe_id = mongo.db.recipe_repository.find_one({"_id": ObjectId(recipe_repository_id)})
    return render_template("view_recipe.html", recipe_id=recipe_id)


# Edit a specific recipe from the db
@app.route("/edit_recipe/<recipe_repository_id>", methods=["GET", "POST"])
def edit_recipe(recipe_repository_id):
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_category": request.form.get("recipe_category"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_prep_time": request.form.get("recipe_prep_time"),
            "recipe_cook_time": request.form.get("recipe_cook_time"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_submitted_by": session["user"]
        }
        mongo.db.recipe_repository.replace_one({"_id": ObjectId(recipe_repository_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for('get_recipes'))

    recipe_id = mongo.db.recipe_repository.find_one({"_id": ObjectId(recipe_repository_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe_id=recipe_id, categories=categories)


# Delete a recipe from the db
@app.route("/delete_recipe/<recipe_repository_id>")
def delete_recipe(recipe_repository_id):
    mongo.db.recipe_repository.delete_one({"_id": ObjectId(recipe_repository_id)})
    flash("Recipe Successfully Removed")
    return redirect(url_for('get_recipes'))


# Add recipe to a favorites array held under the users profile
@app.route("/add_to_favorites/<recipe_repository_id>", methods=["GET", "POST"])
def add_to_favorites(recipe_repository_id):
    if session["user"]:
        current_user = {'username': session['user'].lower()}
        favorite_recipes = mongo.db.users.find_one(current_user)["favorites"]
        if ObjectId(recipe_repository_id) in favorite_recipes:
            flash("This recipe is already in your favorites")
            return redirect(url_for("get_recipes"))
        user_profile = mongo.db.users.find_one(
            {'username': session['user'].lower()})
        mongo.db.users.update_one(
            user_profile, {"$push": {"favorites": ObjectId(
                recipe_repository_id)}})
        flash("Recipe added to favorites")
        return redirect(url_for('get_recipes'))
    return redirect(url_for('get_recipes'))


# Add function to view favorite recipes in profile page


#Untested feature
@app.route("/delete_from_favorites/<recipe_id>")
def delete_from_favorites(recipe_repository_id):
    user_profile = mongo.db.users.find_one(
        {'username': session['user'].lower()})
    mongo.db.users.update_one(
        user_profile, {"$pull": {"favorites": ObjectId(
            recipe_repository_id)}})
    flash("Recipe removed from favorites")
    return redirect(url_for('url_for("profile"), username=session["user"]'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
