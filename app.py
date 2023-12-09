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


@app.route("/")
@app.route("/home")
def home():
    """
    Renders the home template to the user whether logged in or not
    """
    return render_template("home.html")


@app.route("/get_recipes")
def get_recipes():
    """
    Gets all recipes from the db and returns the all_recipes
    template displaying all recipes as cards to the user
    """
    recipes = list(mongo.db.recipe_repository.find())
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/my_recipes")
def my_recipes():
    """
    Gets all user created recipes from the db and renders the
    template to the user
    """
    recipes = list(mongo.db.recipe_repository.find())
    return render_template("my_recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Search all recipes and diplay the results to the user
    """
    query = request.form.get("query")
    recipes = list(mongo.db.recipe_repository.find({
        "$text": {"$search": query}}))
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "post"])
def register():
    """
    Allow a user to register for a profile. Check conducted to determine
    if user already exists and notify the user. If the user doesn't
    exist a new profile is created and the favorites array is emptied
    for the new profile. Once completed the new profile is put into the
    session cookie
    """

    if "user" in session:
        flash("You are already registered.")
        return redirect(url_for("profile", username=session["user"]))

    if request.method == "POST":
        # Check if the username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please try another")
            return redirect(url_for("register"))

        # creates new profile and empty favorites array
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favorites": request.form.get("favorites", [])
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration completed successfully!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Allow an existing user to login. Checks are undertaken
    to determine if the user exists and then ensure the password retained
    matches the user input. If it does not a message is displayed to the user.
    """
    if "user" in session:
        flash("You are already logged in.")
        return redirect(url_for("profile", username=session["user"]))

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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Displays the user logged in and renders the profile template
    """
    # obtain the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})

    # count the number of recipes favorited by the session user
    fav_count = len(username.get('favorites', []))

    # count the number of recipes created by the user
    user = session["user"]
    created_count = mongo.db.recipe_repository.count_documents(
        {'recipe_submitted_by': user})

    # load favorite recipes for session user
    fav = []

    for obj in username["favorites"]:
        recipe = mongo.db.recipe_repository.find_one({"_id": obj})
        fav.append(recipe)

    if session["user"]:
        return render_template(
            "profile.html", username=username,
            fav=fav, fav_count=fav_count,
            created_count=created_count)

    return redirect(url_for("login"))


@app.route("/add_to_favorites/<recipe_repository_id>", methods=["GET", "POST"])
def add_to_favorites(recipe_repository_id):
    """
    Allows user to add a recipe to their "Favorite" array retained within
    the user profile on the db.
    """
    if session["user"]:
        current_user = {'username': session['user'].lower()}
        favorite_recipes = mongo.db.users.find_one(current_user)["favorites"]
        if ObjectId(recipe_repository_id) in favorite_recipes:
            flash("This recipe is already in your favorites")
            return redirect(request.referrer)
        user_profile = mongo.db.users.find_one(
            {'username': session['user'].lower()})
        mongo.db.users.update_one(
            user_profile, {"$push": {"favorites": ObjectId(
                recipe_repository_id)}})
        flash("Recipe added to favorites")
        return redirect(request.referrer)
    return redirect(request.referrer)


@app.route('/delete_from_favorites/<recipe_repository_id>')
def delete_from_favorites(recipe_repository_id):
    """
    Remove a recipe from the users favorite array retained within
    their user profile.
    """
    user_profile = mongo.db.users.find_one(
        {'username': session['user'].lower()})
    mongo.db.users.update_one(
        user_profile, {"$pull": {"favorites": ObjectId(
            recipe_repository_id)}})
    flash("Recipe removed from favorites")
    return redirect(request.referrer)


@app.route("/logout")
def logout():
    """
    log the current user in session out and return them to the login
    page.
    """
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/submit_recipe", methods=["GET", "POST"])
def submit_recipe():
    """
    Submit a new recipe to the recipes repository within the db.
    """
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


@app.route("/view_recipe/<recipe_repository_id>")
def view_recipe(recipe_repository_id):
    """
    Allows single recipe to be displayed in full to the user
    """
    recipe_id = mongo.db.recipe_repository.find_one(
        {"_id": ObjectId(recipe_repository_id)})
    return render_template("view_recipe.html", recipe_id=recipe_id)


@app.route("/edit_recipe/<recipe_repository_id>", methods=["GET", "POST"])
def edit_recipe(recipe_repository_id):
    """
    Allows an existing recipe created by the user to be edited. Checks
    are conducted prior to determine if the user is the on who created it.
    If not the user is denied the ability to edit the recipe and advised
    they do not have permission.
    """
    if request.method == "POST":
        recipe = mongo.db.recipe_repository.find_one(
            {"_id": ObjectId(recipe_repository_id)})

        if session.get("user") != recipe.get("recipe_submitted_by"):
            flash("You are not authorized to edit this recipe.")
            return redirect(request.referrer)

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

        mongo.db.recipe_repository.replace_one(
            {"_id": ObjectId(recipe_repository_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(request.referrer)

    recipe = mongo.db.recipe_repository.find_one(
        {"_id": ObjectId(recipe_repository_id)})
    if session.get("user") != recipe.get("recipe_submitted_by"):
        flash("You are not authorised to edit this recipe.")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe_id=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_repository_id>")
def delete_recipe(recipe_repository_id):
    """
    Selected user created recipe is deleteable from the db
    """
    mongo.db.recipe_repository.delete_one(
        {"_id": ObjectId(recipe_repository_id)})
    flash("Recipe Successfully Removed")
    return redirect(request.referrer)


# Display custom 404 if page does not exist
@app.errorhandler(404)
def page_not_found(e):
    """
    Displays a 404 error page that redirects the user back
    to the home page.
    """
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
