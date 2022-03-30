// Get the checkbox
var checkBox = document.getElementById("hasOffenses");

// Get the output offenses
var defaultoffenses = document.getElementsByClassName("defaultoffenses");
var defaultoffensesCB = document.getElementsByClassName("defaultoffensesCB");

var offenses = document.getElementsByClassName("offenses");
var offensesCB = document.getElementsByClassName("offensesCB");

function myFunction() {
  // If the checkbox is checked, display the output offenses
  if (checkBox.checked == true) {

    for (i = 0; i < defaultoffenses.length; i++) {
      defaultoffenses[i].value = "0";
      defaultoffensesCB[i].checked = false;
    }
  } else {
    for (i = 0; i < offenses.length; i++) {
      offenses[i].value = "0";
      offensesCB[i].checked = false;
    }
  }
}

if (checkBox.checked == true) {
  $(".single-offense").removeClass("show");
  $(".multiple-offense").addClass("show");
}