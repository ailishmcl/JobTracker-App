$(document).ready(function(){
    $('.modal').modal();

    $('.collapsible').collapsible();

    $('.fixed-action-btn').floatingActionButton();

    paintDarkMode();

    $('#dark-mode').click(function() {
      darkMode();
    });

    $("#status-form").on("submit", function(event){
      
      event.preventDefault();

      let formValues= $(this).serialize();
      let formTarget = $('#status-form').attr('action');
      console.log(formValues);

      $.post(formTarget, formValues, function(data){
        window.location.reload();
      });
    });

    setTimeout(function() {
      $('.message').fadeOut('slow');
    }, 10000); // <-- time in milliseconds, 1000 =  1 sec

    // delete message
    $('.del-msg').live('click',function(){
        $('.del-msg').parent().attr('style', 'display:none;');
    });

  });

// Modal Status function for index page

function findMyStatus(jobId){
  let targetUrl = '/jobs/'+jobId+'/edit_status/';
  $.ajax({
    type: 'GET',
    url: targetUrl,
    success: function(res){          
        $('#edit-status-form').html(res);
        $('#status-form').attr('action',targetUrl); 
        
    }
  })
}

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