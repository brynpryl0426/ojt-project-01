$(document).ready(function(){
    $('#submit_form').click(function(e){ 
      e.preventDefault();

      var serializedData = $('#motor_operator_form').serialize();
        $.ajax({  
            type: 'POST',
            url:"/drivers-management/submit-motor-operator/",  
            data:serializedData,
            success:function(data)  
            {
              if(data.error || data.formseterror || data.form_address_error || data.formsetnonformerror){
                $('.error-text').text("");
                $(".non_form_err").text(data.formsetnonformerror);
                  printErrorMsg(data.error);
                  printErrorMsg(data.form_address_error);
                  for (let i = 0; i < $("#id_form-TOTAL_FORMS").val(); i++) {
                    printErrorMsgFormSet(i,data.formseterror[i]);
                  }
                  plate_no_check_duplicates();
                  case_no_check_duplicates();
              }else if(data.success){
                $("#motor_operator_form")[0].reset();
                $("#id_unique_operator_id").val(data.unique_operator_id);
                clearFormsetReset();
                notify_message(data.success, "success");
              }else if (data.integrity_error){
                $('.error-text').text("");
                notify_message(data.integrity_error, "warning");
              }
            }, 
        });  
      });  

      function printErrorMsg (msg) {
          $.each( msg, function( key, value ) {
              $('.'+key.replaceAll(".","")+'_err').text(value);
          });
      }

      function printErrorMsgFormSet (num,msg) {
          $.each( msg, function( key, value ) {
              $('.'+"id_form-"+num+"-"+key.replaceAll(".","")+'_err').text(value);
          });
      }
});