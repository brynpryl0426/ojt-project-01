$('#btnUploader').click(function() {
    $('#btnUploader').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Uploading...').attr('disabled', true);
    $("#uploadDataForm").submit();
  });