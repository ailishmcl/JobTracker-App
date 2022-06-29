$(document).ready(function(){
    $('.modal').modal();

    $('.fixed-action-btn').floatingActionButton();

    paintDarkMode();

    $('#dark-mode').click(function() {
      darkMode();
    });
  });

  
// Dark mode on local storage

function darkMode() {
  if(localStorage.getItem('darkMode') === null )
    localStorage.setItem('darkMode', false);
  toggleDarkMode();
  paintDarkMode();
}

function paintDarkMode() {
  let darkMode = getDarkMode();
  var element = document.body;
  if(darkMode) {
    element.classList.add('dark-mode');
  } else {
    element.classList.remove('dark-mode');
  }
}

function getDarkMode() {
  return JSON.parse(localStorage.getItem('darkMode'));
}

function toggleDarkMode() {
  let darkMode = getDarkMode();
  darkMode = !darkMode;
  localStorage.setItem('darkMode', darkMode);
  return getDarkMode();
}