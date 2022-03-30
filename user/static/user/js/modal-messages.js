function alertinfomessage(title, message) {
  $("#centralModalInfo").modal('show');
  $(".head-title").text(title);
  $(".modal-message").text(message);
}

function alertdeletemessage(title, message) {
  $("#centralModalDelete").modal('show');
  $(".head-title").text(title);
  $(".modal-message").text(message);
}