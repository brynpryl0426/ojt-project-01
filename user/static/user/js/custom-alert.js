function notify_message(message, message_type) {
  if (message_type === "success") {
    toastr.success(message, "", { positionClass: "md-toast-top-center" });
    $("#toast-container").attr("class", "md-toast-top-center");
  } else if (message_type === "info") {
    toastr.info(message, "", { positionClass: "md-toast-top-center" });
    $("#toast-container").attr("class", "md-toast-top-center");
  } else if (message_type === "warning") {
    toastr.warning(message, "", { positionClass: "md-toast-top-center" });
    $("#toast-container").attr("class", "md-toast-top-center");
  } else if (message_type === "error") {
    toastr.error(message, "", { positionClass: "md-toast-top-center" });
    $("#toast-container").attr("class", "md-toast-top-center");
  }
}
