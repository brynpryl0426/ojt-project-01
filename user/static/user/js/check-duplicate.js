function plate_no_check_duplicates() {
  var counter = $("#id_form-TOTAL_FORMS").val();
  var myarray = [];
  for (i = 0; i < counter; i++) {
    $(".id_form-" + i + "-plate_no_dup_err").text("");
    myarray[i] = document.getElementById("id_form-" + i + "-plate_no").value;
  }
  for (i = 0; i < counter; i++) {
    var flag = false;
    for (j = 0; j < counter; j++) {
      if (i == j || myarray[i] == "" || myarray[j] == "") {
        continue;
      }
      if (myarray[i] == myarray[j]) {
        flag = true;
        $(".id_form-" + i + "-plate_no_dup_err").text(
          "Plate no. has duplicated values."
        );
      }
    }
    if (flag == false) {
      $(".id_form-" + i + "-plate_no_dup_err").text("");
    }
  }
}

function case_no_check_duplicates() {
  var counter = $("#id_form-TOTAL_FORMS").val();
  var myarray = [];
  for (i = 0; i < counter; i++) {
    $(".id_form-" + i + "-case_no_dup_err").text("");
    myarray[i] = document.getElementById("id_form-" + i + "-case_no").value;
  }
  for (i = 0; i < counter; i++) {
    var flag = false;
    for (j = 0; j < counter; j++) {
      if (i == j || myarray[i] == "" || myarray[j] == "") {
        continue;
      }
      if (myarray[i] == myarray[j]) {
        flag = true;
        $(".id_form-" + i + "-case_no_dup_err").text(
          "Case no. has duplicated values."
        );
      }
    }
    if (flag == false) {
      $(".id_form-" + i + "-case_no_dup_err").text("");
    }
  }
}
