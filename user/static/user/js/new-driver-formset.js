const vehicleForm = document.getElementsByClassName("vehicle-form");
const mainForm = document.querySelector("#motor_operator_form");
const addVehicleFormBtn = document.querySelector("#add-vehicle-form");

$('.vehicle-form').hide();

addVehicleFormBtn.addEventListener("click", function (event) {
  event.preventDefault();
  
  let formCount = $(".vehicle-form:visible").length + 1;
 
  for (let i = 0; i < formCount; i++) {
    if(formCount>3){
      continue;
    }
    $(".vehicle-form").eq(i).show();
  }
});

$(document).on('click', '.delete-vehicle-form', function () {
  $(this).parents('.vehicle-form').hide().insertAfter($(".vehicle-form:last"));
  $(".error-text").text("");
  $(this).parents('.vehicle-form').find('input').val("");
  $(this).parents('.vehicle-form').find('label').removeClass("active");
  $(this).parents('.vehicle-form').find('select').val(null).trigger('change');
});

function clearFormsetReset(){
  $('.vehicle-form').hide();
  $(".error-text").text("");
  $("label").removeClass("active");
  $('select').val(null).trigger('change');
}