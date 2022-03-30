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
    $("#vehicle").select2({
      ajax: {
        url: "/traffic-violations-management-monitoring/vehicle-search/",
        dataType: "json",
        processResults: function (data) {
          return {
            results: $.map(data, function (item) {
              return {
                id: item.id,
                text: item.owner__fullname,
                case_no: item.case_no,
                plate_no: item.plate_no,
                address: driver_address(
                  item.owner__city,
                  item.owner__barangay,
                  item.owner__addressline
                ),
              };
            }),
          };
        },
      },
      minimumInputLength: 2,
      placeholder: "Vehicle Owner",
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
  
  
    $("#vehicle").on('change', function() {
      
      $("#casenolabel").addClass('active')
      $("#platenolabel").addClass('active')
  
      var data =$('#vehicle').select2('data');
      $("#caseno").val(data[0].case_no);
      $("#plateno").val(data[0].plate_no);
      
      if($("#caseno").val()==''){
        $("#casenolabel").removeClass('active');
      }

      if($("#plateno").val()==''){
        $("#platenolabel").removeClass('active');
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
          "<div class='select2-result-repository__statistics'>" +
          "<div class='select2-result-repository__caseno'><i class='fas fa-archway text-warning'></i> </div>" +
          "<div class='select2-result-repository__plateno'><i class='fas fa-motorcycle text-danger'></i> </div>" +
          "</div>" +
          "</div>" +
          "</div>"
      );
  
      if(isEmptyOrSpaces(repo.case_no)){
        repo.case_no = "N/A";
      }
  
      if(isEmptyOrSpaces(repo.plate_no)){
        repo.plate_no = "N/A";
      }
  
      $container.find(".select2-result-repository__driver").text(repo.text);
      $container.find(".select2-result-repository__address").append(repo.address);
      $container.find(".select2-result-repository__caseno").append(repo.case_no);
      $container
        .find(".select2-result-repository__plateno")
        .append("Plate no. " + repo.plate_no);
  
      return $container;
    }
  
    function formatRepoSelection(repo) {
      return repo.fullname || repo.text;
    }
  });