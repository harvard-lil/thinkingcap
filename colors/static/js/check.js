document.onkeydown = function(evt) {
    evt = evt || window.event;
    if (evt.key == 'c') {
      document.getElementById('confirmed-color').click();
    } else if (evt.key == 'n') {
      document.getElementById('confirmed-not-color').click();
    }
};