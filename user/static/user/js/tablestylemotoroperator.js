$("#dtMaterialDesign").DataTable({ paging: false,  "searching": false });
  
  function TableTitleSetter(table_title,linktarget){
    $("#dtMaterialDesign_wrapper .row")
    .find("div")
    .first()
    .append(
      '<div class="md-form">'+
      '<h3 class="dark-grey-text font-weight-bold table-label">'+
      table_title+
      '&nbsp;<a href="'+linktarget+'">'+
      '<i class="fas fa-plus text-success"></i>'+
      '</a>'+
      '</h3>'+
      '</div>'
    );
  }
