# Pizza-Stop-Milestone-Project-3
## Back End Development Project

For my third milestone project I have designed and developed a website using HTML, CSS and JavaScript, Python, Flask and MongoDB. The purpose of the site is to bring Pizza lovers together to share dough recipes, topping combinations and side dishes. Users are able to create a user profile to upload, amend and delete their own recipes whilst being able to add other users uploads to their recipe collection, but preventing them from deleting or amending them.

![Visual Representation](documentation/visual-pizza-stop.png)

[Live version of the site](https://pizza-stop-5bc4c092c1c7.herokuapp.com/)

---
## User Experience (UX) & Design
---
### User Stories
- First Time Visitor

    - As a first time visitor, I would like to be able to understand the purpose of the website.
    - As a first time visitor, I would like to register for a free account.
    - As a first time visitor, start browsing the existing recipes.

- Returning Visitor

    - As a returning visitor, I would like to be able to add existing recipes to my own collection.
    - As a returning visitor, I would like to view a recipe in full.
    - As a returning visitor, I would like to be able to create a new recipe or amend and/or delete recipes I have created.

- Website Administrator

    - As the website administrator, I would like to be able to manage the list of users registered to the site.

### Color Scheme
The colors selected for the color palette are based on the Materialize color palette, specifically the teal palette:

![Color Palette](documentation/color-palette.png)


### Typography
Google Fonts was used to import the 'Bebas Neue' and the 'Ubuntu' fonts into the style.css file for use across all pages.

### Wireframes
Each link contains wireframes for mobile, tablet and desktop.
- ### Home
![Home](documentation/wireframes/home.png)
- ### Register
![Register](documentation/wireframes/register.png)
- ### Login
![Login](documentation/wireframes/login.png)
- ### Profile
![Profile](documentation/wireframes/profile.png)
- ### Recipes Library
![Recipes Library](documentation/wireframes/recipes_library.png)
- ### Add Recipe
![Add Recipe](documentation/wireframes/add_recipe.png)
- ### My Recipes
![My Recipes](documentation/wireframes/my_recipes.png)
- ### View Recipe
![View Recipe](documentation/wireframes/view_recipe.png)
- ### Edit Recipe
![Edit Recipe](documentation/wireframes/edit_recipe.png)
- ### 404
![404](documentation/wireframes/404.png)
---
## Features
---
### Home Page
The Home Page is the introduction to the website, providing an insight into its purpose and providing the user the option to login or register.

![Home page image](documentation/screenshots/home_screenshot.png)

### Nav bar
The navigation bar is situated at the top of the page on all pages. It changes from a toggle button to a row of options on large screens. Once logged in more options are availabe to the user.

![Nav Bar Logged Out image](documentation/screenshots/nav_bar_logged_out.png)
![Nav Bar Logged In image](documentation/screenshots/nav_bar_logged_in.png)

### Footer
The footer is present on each page displays the websites slogan and also displays the same menu options as the header with links to social media profiles.

![Footer Logged Out image](documentation/screenshots/footer_logged_out.png)
![Footer Logged In image](documentation/screenshots/footer_logged_in.png)

### Register Page
The Register page is where new users can go to sign up for an account.

![Register page image](documentation/screenshots/register_screenshot.png)

### Login Page
Similar to the Register page in styling, the Login page allows an existing user to log into the service and then directs the user to the profile page.

![Login page image](documentation/screenshots/login_screenshot.png)

### Profile Page
The Profile page displays the in session users name, the number of recipes they have favorited and the number of recipes they have created. It also shows each recipe favorited in card form

![Profile page image](documentation/screenshots/profile_screenshot.png)

### Recipes Library page
The Recipes Library page displays all recipes in the db in card form. Each card has two buttons, one to view the recipe in full and the other to add to the in session users favorite list.

![Recipes Library page image](documentation/screenshots/recipes_library_screenshot.png)

### Add Recipe page
The Add Recipe page allows an active user that is signed in to submit their own recipes. They can input the title, assign it to one of the categories, provide times for preparation and cooking, number of people served, a description of the recipe, the ingredients with the option of adding or removing items as necessary, the method steps which also allows the option of adding or removing steps as necessary and the option to provide a web link to an image.

![Add Recipe page image](documentation/screenshots/submit_recipe_screenshot.png)

### My Recipes page
The My Recipes page displays all user in session created recipes in card form with the same two buttons from the recipes library page, one to view the recipe in full and the other to add to the in session users favorite list.

![My Recipes page image](documentation/screenshots/my_recipes_screenshot.png)

### View Recipe page
The View Recipe page takes the recipe and displays it full screen for the user. If the user in session created the recipe, they can choose to edit the recipe or if so delete the recipe entierly. Prior to deletion the user is advised that this is nothing they can't undo this action before requiring user input before proceeding with or cancelling the request to delete.

![View Recipe page image](documentation/screenshots/view_recipe_screenshot.png)

### Edit Recipe page
THe Edit Recipe page allows the user who has created the recipe to be able to edit the recipe with the ability to amend each item within the db, similar to the create recipe page.

![Edit Recipe page image](documentation/screenshots/edit_recipe_screenshot.png)

### 404 Page
A custom 404 page has been created and assigned via GitHub to load whenever a non-existent page is requested.

![404 page image](documentation/screenshots/404_screenshot.png)

---
## Technologies Used
---
### Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Programs Used
- [Balsamiq](https://balsamiq.com/) was used for pre-visualisation of the pages.
- [Google Fonts](https://fonts.google.com/) was used to import the the 'Russo One' and 'Exo 2' fonts into the style.css file.
- [Font Awesome](https://fontawesome.com/) was utilised for icons used on the site for the social media icons.
- [Materialize](https://materializecss.com/) was used for responsive grids, navigation elements, cards, CSS and button elements.
- [Git](https://git-scm.com/) was used for version control. I utilised the CLI terminal in Visual Studio to commit and push to GitHub.
- [Visual Studio Code](https://code.visualstudio.com/) was used as the development enviroment to develop the site.
- [GitHub](https://github.com/) was used as the repository for the project after being pushed from GitPod.
- [Heroku](https://www.heroku.com/) was used to deploy the python application.
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) the micro web framework written in Python.
- [Jinja](https://jinja.palletsprojects.com/) the web template engine for the Python programming language
- [Adobe Express](https://www.adobe.com/express/create/logo) used to produce the website image.
- [TINYURL](https://tinyurl.com/app) used to shorten the default image used if no recipe image provided.

---
## Testing
---
### Validator Testing
#### HTML
HTML Markup Validator results:
- [index.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fahendley84.github.io%2FFormula-1-Card-Battles%2Findex.html)
- [game.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fahendley84.github.io%2FFormula-1-Card-Battles%2Fgame.html)
- [player_win.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fahendley84.github.io%2FFormula-1-Card-Battles%2Fplayer_win.html)
- [computer_win.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fahendley84.github.io%2FFormula-1-Card-Battles%2Fcomputer_win.html)
- [404.html](https://validator.w3.org/nu/?doc=https%3A%2F%2Fahendley84.github.io%2FFormula-1-Card-Battles%2F404.html)


#### CSS
- [CSS Validation](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fahendley84.github.io%2FFormula-1-Card-Battles%2Fassets%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)


#### JavaScript
- The JavaScript used in this project has been tested on both [JSLint](https://www.jslint.com/) and [JSHint](https://jshint.com/) with no concerns.

#### Python
- The Python used in this project has been tested on the [CI Python Linter](https://pep8ci.herokuapp.com/) to ensure it is PEP8 compliant.

### Browser Compatibility
The site has been tested on the following browsers (latest builds as of 09/12/2023):
- Google Chrome version Version 120.0.6099.71 (Official Build) (64-bit)
- Mozilla Firefox Version 120.0.1 (64-bit)
- Microsoft Edge Version 119.0.2151.97 (Official build) (64-bit)
- Apple Safari (Latest build on iOS 17.1)

### Manual Testing and Results
Here is a table of the manual testing done on the site to determine if all features work as described and designed:



### User Story Testing
|User Story|Screenshot|||
|---|---|---|---|
|**First Time Visitor**|
|As a first time visitor, I would like to be able to understand the purpose of the website.|![Home page](documentation/screenshots/home_screenshot.png)|||
|As a first time visitor, I would like to register for a free account.|![Registration page](documentation/screenshots/register_screenshot.png)|||
|As a first time visitor, start browsing the existing recipes.|![Recipe Library page](documentation/screenshots/recipes_library_screenshot.png)|||
|**Returning Visitor**|
|As a returning visitor, I would like to be able to add existing recipes to my own collection.|![Profile page](documentation/screenshots/profile_screenshot.png)|![Recipe Library page](documentation/screenshots/recipes_library_screenshot.png)||
|As a returning visitor, I would like to view a recipe in full.|![View Recipe page](documentation/screenshots/view_recipe_screenshot.png)|||
|As a returning visitor, I would like to be able to create a new recipe or amend and/or delete recipes I have created.|![Submit Recipe page](documentation/screenshots/submit_recipe_screenshot.png)|![Edit Recipe page](documentation/screenshots/edit_recipe_screenshot.png)|![Delete Recipe prompt](documentation/screenshots/delete_recipe_prompt.png)|
|**Website Administrator**|
|As the website administrator, I would like to be able to manage the list of users registered to the site.|At present this is done on the database server side|![Image of user screen on db](documentation/screenshots/database_user_management.png)||

### Lighthouse Test
|Page|Device|Lighthouse Result|
|---|---|---|
|Home|Mobile|![Index Mobile Results](documentation/lighthouse/index_mobile.png)|
|Home|Desktop|![Index Desktop Results](documentation/lighthouse/index_desktop.png)|
|Register|Mobile|![Game Mobile Results](documentation/lighthouse/game_mobile.png)|
|Register|Desktop|![Game Desktop Results](documentation/lighthouse/game_desktop.png)|
|Login|Mobile|![Player Win Mobile Results](documentation/lighthouse/player_win_mobile.png)|
|Login|Desktop|![Player Win Desktop Results](documentation/lighthouse/player_win_desktop.png)|
|Profile|Mobile|![Computer Win Mobile Results](documentation/lighthouse/computer_win_mobile.png)|
|Profile|Desktop|![Computer Win Desktop Results](documentation/lighthouse/computer_win_desktop.png)|
|Recipes Library|Mobile|![Computer Win Mobile Results](documentation/lighthouse/computer_win_mobile.png)|
|Recipes Library|Desktop|![Computer Win Desktop Results](documentation/lighthouse/computer_win_desktop.png)|
|Add Recipe|Mobile|![Computer Win Mobile Results](documentation/lighthouse/computer_win_mobile.png)|
|Add Recipe|Desktop|![Computer Win Desktop Results](documentation/lighthouse/computer_win_desktop.png)|
|My Recipes|Mobile|![Computer Win Mobile Results](documentation/lighthouse/computer_win_mobile.png)|
|My Recipes|Desktop|![Computer Win Desktop Results](documentation/lighthouse/computer_win_desktop.png)|
|View Recipe|Mobile|![Computer Win Mobile Results](documentation/lighthouse/computer_win_mobile.png)|
|View Recipe|Desktop|![Computer Win Desktop Results](documentation/lighthouse/computer_win_desktop.png)|
|Edit Recipe|Mobile|![Computer Win Mobile Results](documentation/lighthouse/computer_win_mobile.png)|
|Edit Recipe|Desktop|![Computer Win Desktop Results](documentation/lighthouse/computer_win_desktop.png)|
|404|Mobile|![404 Mobile Results](documentation/lighthouse/404_mobile.png)|
|404|Desktop|![404 Desktop Results](documentation/lighthouse/404_desktop.png)|

### Resposiveness
The website has been tested on multiple web browsers, including Google Chrome, Microsoft Edge and Mozilla Firefox. Google Chrome Developer Tools have been used to simulate multiple different device screen sizes such as iPhone SE, Pixel 5, iPad Air and iPad Mini. It has been tested physically on an iPhone 12 Pro, 3rd Gen iPad and on desktop screens 2560 x 1440 pixels and 1920 x 1080 pixels.

### Bugs
|Bug Number|Expected|Actual|Fix|
|---|---|---|---|
|Bug 1|Nationality should display the drivers Nationality|Nationality on the active computer card was displaying a number|The code was pointing to the number of drivers championships rather than the nationality. Amending the code to look at the nationality inside the active card object resolved the issue|
|Bug 2|The game function should continue until either the computer or the player has all 20 cards|After approximately 10 games the game would stop unexpectedly and the console would display 'Uncaught TypeError: Cannot read properties of undefined (reading 'img1')'|I reached out to the #project-milestone-2 channel for some guidance. After some initial guidance from Joy Zadan I was able to resolve the issue by moving the displayImages and displayDriverStats into the assignCurrentCard function. I was then able to further improve the code with the help of Joy Zadan to a length check of the playerCards and currentCards to ensure they were greater than zero before assigning the next random card available|
|Bug 3|The message and score boards should remain in their own separate containers|Overlapping text between the message board and the scoreboard|the height of the message board container had been set to 30px. I changed this to the minimum height which resolved the issue|

### Unfixed Bugs
As of the 19/08/2023 there are no known bugs present.

---
## Deployment
---
### How the site was deployed

The site was deployed to GitHub Pages. The steps to deploy are as follows:

- In the [GitHub repository](https://github.com/AHendley84/Formula-1-Card-Battles), navigate to the Settings tab
- Under the heading "Code and automation", select "Pages".
- From the source section drop-down menu, select the Main Branch, then click "Save".
- The page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found [here](https://ahendley84.github.io/Formula-1-Card-Battles/)

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/AHendley84/Formula-1-Card-Battles)
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI, and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
   - `git clone https://github.com/AHendley84/Formula-1-Card-Battles.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

Once the extension is installed or you have it already, click --> [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/AHendley84/Formula-1-Card-Battles)

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/dougyb83/minesweeper)
2. At the top right of the repository but below the navbar, locate the "Fork" button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

---
## Credits & Acknowledgments
---
- Massive thank you to [astral-g](https://github.com/astral-g) for his [Top Trumps Game](https://github.com/astral-g/Top-Trumps-Game) which allowed me to base and modify my own game on.
- Driver and Team Logo images courtsey of skysports.com.
- Driver stats and information courtsey of Formula1.com.
- Carbon fibre background image courtsey of [Freepik.com](https://www.freepik.com/free-photos-vectors/carbon-fibre-texture).
- Background image used in 404.html courtesy of [CNN.com](https://edition.cnn.com/2018/08/30/motorsport/formula-one-crashes-defined-sport-halo-spt-intl/index.html).
- Background image used in player_win.html courtsey of [topgear.com](https://www.topgear.com/car-news/motorsport/tgs-five-favourite-f1-podium-celebrations).
- Background image used in computer_win.html courtsey of [autosport.com](https://www.autosport.com/f1/news/lauda-slams-sabotage-talk-after-hamiltons-malaysian-gp-failure-5033191/5033191/).
- Thanks to [Stack Overflow](https://stackoverflow.com/questions/4919076/outline-effect-to-text) for help on applying the text-shadow to the text on the 404, Player Win and Computer Win pages.
- Credit to [W3 Schools](https://www.w3schools.com/jsref/prop_style_cursor.asp) for the cursor change property guidance.
- Thanks to [GitHub](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site) for this handy guide to adding your own custom 404 page.
- Thank you to [Joy Zadan on Slack](https://code-institute-room.slack.com/archives/C7HD37Q1F/p1691322584027999) for helping me to resolve the second bug identified in my JavaScript code.