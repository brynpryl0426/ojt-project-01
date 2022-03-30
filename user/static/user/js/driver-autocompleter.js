function isEmptyOrSpaces(str) {
  return str === null || str.match(/^ *$/) !== null;
}
function driver_address(city, barangay, addressline) {
  var name = "";
  if (isEmptyOrSpaces(addressline)) {
    name = `${city}, ${barangay}`;
  } else {
    name = `${city}, ${barangay}, ${addressline}`;
  }
  return name;
}
$(document).ready(function () {
  $("#driver").select2({
    ajax: {
      url: "/traffic-violations-management-monitoring/driver-search/",
      dataType: "json",
      processResults: function (data) {
        return {
          results: $.map(data, function (item) {
            return {
              id: item.id,
              text: item.fullname,
              address: driver_address(
                item.city,
                item.barangay,
                item.addressline
              ),
            };
          }),
        };
      },
    },
    minimumInputLength: 2,
    placeholder: "Traffic Violator",
    theme: "material",
    width: "100%",
    allowClear: true,
    templateResult: formatRepo,
    templateSelection: formatRepoSelection,
    closeOnSelect: true,
    language: {
      noResults: function() {
          return "<a href='/drivers-management/new-motor-operator/' target='_blank' class='w-100'>Add New Motor Operator</a>";
     }
    },
      escapeMarkup: function (markup) {
        return markup;
    }
  });


  $("#driver").on('change', function() {
    
    $("#addresslabel").addClass('active');

    var data =$('#driver').select2('data');
    $("#address").val(data[0].address);
    
    if($("#address").val()==''){
      $("#addresslabel").removeClass('active');
    }

  });

  function formatRepo(repo) {
    if (repo.loading) {
      return repo.text;
    }

    var $container = $(
      "<div class='select2-result-repository clearfix'>" +
        "<div class='select2-result-repository__meta'>" +
        "<strong class='select2-result-repository__driver'></strong>" +
        "<div class='select2-result-repository__address'><i class='fas fa-map-marker-alt text-success'></i> </div>" +
        "</div>" +
      "</div>"
    );


    $container.find(".select2-result-repository__driver").text(repo.text);
    $container.find(".select2-result-repository__address").append(repo.address);

    return $container;
  }

  function formatRepoSelection(repo) {
    return repo.fullname || repo.text;
  }

  $("#date_apprehended").on('change', function() {
    $("#date_apprehendedlabel").addClass('active');

    if($("#date_apprehended").val()==''){
      $("#date_apprehendedlabel").removeClass('active');
    }
  });
});