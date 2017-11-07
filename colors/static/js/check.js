document.onkeydown = function(evt) {
    evt = evt || window.event;
    if (evt.key == 'c') {
      var shoutout = document.getElementById('its-a-color');
      shoutout.style.display = "inline";
      setTimeout(function(){
        document.getElementById('confirmed-color').click();
        shoutout.style.display = "none";
      }, 500);


    } else if (evt.key == 'n') {
      var shoutout = document.getElementById('its-not-a-color');
      shoutout.style.display = "inline";
      setTimeout(function(){
        document.getElementById('confirmed-not-color').click();
        shoutout.style.display = "none";
      }, 500);
    }
};