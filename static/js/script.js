$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('select').formSelect();
  });

/** JavaScript to operate the add another ingredient */
let addIngredientsBtn = document.getElementById('addIngredientsBtn');
let ingredientList = document.querySelector('.ingredientList');
let ingredientDiv = document.querySelectorAll('.ingredientDiv')[0];

addIngredientsBtn.addEventListener('click', function(){
  let newIngredients = ingredientDiv.cloneNode(true);
  let inputIngredients = newIngredients.getElementsByTagName('input')[0];
  inputIngredients.value = '';
  ingredientList.appendChild(newIngredients);
});

/** JavaScript to operate the add another method step */
let addMethodBtn = document.getElementById('addMethodBtn');
let methodList = document.querySelector('.methodList');
let methodDiv = document.querySelectorAll('.methodDiv')[0];

addMethodBtn.addEventListener('click', function(){
  let newMethod = methodDiv.cloneNode(true);
  let inputMethod = newMethod.getElementsByTagName('input')[0];
  inputMethod.value = '';
  methodList.appendChild(newMethod);
});