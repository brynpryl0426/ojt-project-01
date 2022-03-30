$(".report-selection").select2({
  minimumResultsForSearch: Infinity,
  theme: "material",
  placeholder: "Select Report",
  width: "100%",
});

$("#date_one").pickadate({
    selectYears: 200,
    format: "mmmm dd, yyyy",
  });

$("#date_two").pickadate({
  selectYears: 200,
  format: "mmmm dd, yyyy",
});

$("#report_selection").on("change", function () {
    if($("#report_selection option:selected").val()==4){
        $(".custom-filter").show();
    }
    else{
        $(".custom-filter").hide();
    }
});