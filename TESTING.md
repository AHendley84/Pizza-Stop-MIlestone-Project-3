## Testing
---
### Validator Testing
#### HTML
HTML Markup Validator results:

<details>
<summary>Home</summary>

Identified an issue where by a section tag was causing an error on the base template containing the nav bar, footer and flash messages. Changing this to a div tag resolved the error and resulted in no further warnings or errors.
![Home](documentation/testing/html/home_html.png)

</details>

<details>
<summary>Register</summary>

![Register](documentation/testing/html/register_html.png)

</details>

<details>
<summary>login</summary>

![Login](documentation/testing/html/login_html.png)

</details>

<details>
<summary>Profile</summary>

Identified that the ```alt``` tag was missing from the ```img``` attribute, this was easily rectified. The Profile page is failing the W3C check as it wasn't able to  conduct the check with a user logged in, causing a 500 error. However, a direct code input validation, higlighted an erent ```i``` and  ```/div```.
![Profile](documentation/testing/html/profile_html.png)

</details>

<details>
<summary>Recipes Library</summary>

Identified that the ```alt``` tag was missing from the ```img``` attribute, this was easily rectified.
![Recipes Library](documentation/testing/html/recipes_library_html.png)

</details>

<details>
<summary>Add Recipe</summary>

Identified two errors on the page, both in relation to the drop down menu for the category functions. Attempts to rectify this issue resulted in further errors. I've tested that the dropdown works as it should so the errors remain at present.
![Add Recipe](documentation/testing/html/add_recipe_html.png)

</details>

<details>
<summary>My Recipes</summary>

![My Recipes](documentation/testing/html/my_recipes_html.png)

</details>

<details>
<summary>View Recipe</summary>

Identified that the ```alt``` tag was missing from the ```img``` attribute, this was easily rectified. 
![View Recipe](documentation/testing/html/view_recipe_html.png)

</details>

<details>
<summary>Edit Recipe</summary>

![Edit Recipe](documentation/testing/html/edit_recipe_html.png)

</details>

<details>
<summary>404</summary>

Due to the nature of the 404 error, I was unable to submit this through the URL check on W3C. However, I did submit the code via direct code input, and aside from the issues with the Jinja code and a trailing ```/``` on the font awesome link, there are no issues identified.
![404](documentation/testing/html/404_html.png)

</details>



#### CSS
- The CSS used in this project was tested with [W3c CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input) with no concerns.


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

### Manual Testing Results
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

### Unfixed Bugs
As of the 10/12/2023 the only known bug present is the issue with the Add Recipe dropdown.

Back to [README.md](README.md).