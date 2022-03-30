$("#modalLoginForm").modal("show");
new WOW().init();

$("#modalLoginForm").on("shown.bs.modal", function () {
  $("#orangeForm-email").focus();
});
