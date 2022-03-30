$(document).ready(function () {
  $("#apprehending_officer").select2({
    ajax: {
      url: "/traffic-violations-management-monitoring/officer-search/",
      dataType: "json",
      processResults: function (data) {
        return {
          results: $.map(data, function (item) {
            return {
              id: item.id,
              text: item.fullname,
            };
          }),
        };
      },
    },
    minimumInputLength: 2,
    placeholder: "Apprehending Officer",
    theme: "material",
    width: "100%",
    allowClear: true,
  });
});
