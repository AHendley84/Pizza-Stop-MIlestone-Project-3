$(document).ready(function () {
    // Materialize side nav jQuery
    $(".sidenav").sidenav({ edge: "right" });
    // Materialize select jQuery
    $('select').formSelect();
    // Materialize modal jQuery
    $('.modal').modal();
    // Function to clear flashed messages after 5 seconds (5000 milliseconds)
    setTimeout(function () {
        $('.flashes').fadeOut('slow', function () {
            $(this).remove();
        });
    }, 5000);
    
    /*
    The JavaScript for validation of the Materialize drop down was based on the code from CI build along for the task manager mini-project.
    */

    // Validation for Materialize drop down
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});



/*
The JavaScript for the addition button function is based on the code in the YouTube video from Raddy:
https://raddy.dev/blog/how-to-build-a-recipe-blog-using-node-js-and-mongodb-express-ejs-mongoose-crud/
I repurposed the code for the addition button to create the remove button
*/

// JavaScript to operate the add and remove ingredient
let addIngredientsBtn = document.getElementById('addIngredientsBtn');
let ingredientList = document.querySelector('.ingredientList');
let ingredientDiv = document.querySelectorAll('.ingredientDiv')[0];

addIngredientsBtn.addEventListener('click', function () {
    let newIngredients = ingredientDiv.cloneNode(true);
    let inputIngredients = newIngredients.getElementsByTagName('input')[0];
    inputIngredients.value = '';
    ingredientList.appendChild(newIngredients);
});

removeIngredientsBtn.addEventListener('click', function () {
    let ingredients = ingredientList.querySelectorAll('.ingredientDiv');
    if (ingredients.length > 1) {
        ingredientList.removeChild(ingredients[ingredients.length - 1]);
    }
});

// JavaScript to operate the and remove method
let addMethodBtn = document.getElementById('addMethodBtn');
let methodList = document.querySelector('.methodList');
let methodDiv = document.querySelectorAll('.methodDiv')[0];

addMethodBtn.addEventListener('click', function () {
    let newMethod = methodDiv.cloneNode(true);
    let inputMethod = newMethod.getElementsByTagName('input')[0];
    inputMethod.value = '';
    methodList.appendChild(newMethod);
});

removeMethodBtn.addEventListener('click', function () {
    let methods = methodList.querySelectorAll('.methodDiv');
    if (methods.length > 1) {
        methodList.removeChild(methods[methods.length - 1]);
    }
});