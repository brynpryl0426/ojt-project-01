$("#dtMaterialDesign").DataTable({ paging: false });
$("#dtMaterialDesign_wrapper")
  .find("label")
  .each(function () {
    $(this).parent().append($(this).children());
  });
  
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


$(".dataTables_filter")
  .find("input")
  .each(function () {
    $("input").attr("placeholder", "Search");
    $("input").removeClass("form-control-sm");
    $("input").addClass("search-input");
  });
$(
  "#dtMaterialDesign_wrapper .dataTables_length, #dt-material-checkbox_wrapper .dataTables_length"
).addClass("d-flex flex-row");
$(
  "#dtMaterialDesign_wrapper .dataTables_filter, #dt-material-checkbox_wrapper .dataTables_filter"
)
  .find("label")
  .remove();
$(
  "#dtMaterialDesign_wrapper .dataTables_filter, #dt-material-checkbox_wrapper .dataTables_filter"
).addClass("md-form");
