var $ctxB = $("#barChart");
var barChart;
function load_data_per_year(year) {
  $.ajax({
    url: "/dashboard-monthly-graph/"+year,
    success: function (data) {
      var ctx = $ctxB[0].getContext("2d");

      if (barChart) {
        barChart.destroy();
      }

      barChart = new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.labels,
          datasets: [
            {
              label: "# of Violations",
              data: data.data,
              backgroundColor: [
                "rgba(3, 169, 244, 0.3)",
                "rgba(244, 67, 54, 0.3)",
                "rgba(233, 30, 99, 0.3)",
                "rgba(156, 39, 176, 0.3)",
                "rgba(63, 81, 181, 0.3)",
                "rgba(0, 188, 212, 0.3)",
                "rgba(0, 150, 136, 0.3)",
                "rgba(76, 175, 80, 0.3)",
                "rgba(255, 152, 0, 0.3)",
                "rgba(255, 235, 59, 0.3)",
                "rgba(255, 152, 0, 0.3)",
                "rgba(121, 85, 72, 0.3)",
              ],
              borderColor: [
                "rgba(3, 169, 244, 1)",
                "rgba(244, 67, 54, 1)",
                "rgba(233, 30, 99, 1)",
                "rgba(156, 39, 176, 1)",
                "rgba(63, 81, 181, 1)",
                "rgba(0, 188, 212, 1)",
                "rgba(0, 150, 136, 1)",
                "rgba(76, 175, 80, 1)",
                "rgba(255, 152, 0, 1)",
                "rgba(255, 235, 59, 1)",
                "rgba(255, 152, 0, 1)",
                "rgba(121, 85, 72, 1)",
              ],
              borderWidth: 2,
            },
          ],
        },
        options: {
          legend: {
            display: false,
          },
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
              },
            ],
          },
          title: {
            display: true,
            text: "Recorded Violations Per Month",
          },
        },
      });
    },
  });
}
load_data_per_year(2021);
$("#year").on("change", function () {
  load_data_per_year($("#year option:selected").text());
});
// End of Barchart
var $ctxP = $("#doughnutChart");
var pieChart;
function load_data_custom(year,month){
  $.ajax({
    url: "/dashboard-custom-date/"+year+"/"+month,
    success: function (data) {

      if(data.data.length==0){
        $(".pie-container").hide();
        $(".no-data").show();
      }else{
        $(".pie-container").show();
        $(".no-data").hide();
      }

      var context = $ctxP[0].getContext("2d");
      var coloR = [];

      var dynamicColors = function() {
        var r = Math.floor(Math.random() * 255);
        var g = Math.floor(Math.random() * 255);
        var b = Math.floor(Math.random() * 255);
        return "rgba(" + r + "," + g + "," + b + ",0.8)";
    };

      for (var i in data.data) {
        coloR.push(dynamicColors());
      }

      if (pieChart) {
        pieChart.destroy();
      }
      pieChart = new Chart(context, {
        type: 'pie',
          data: {
            labels: data.labels,
            datasets: [{
              data: data.data,
              backgroundColor: coloR,
              hoverBackgroundColor: coloR,
            }]
          },
          options: {
            responsive: true,
            title: {
              display: true,
              text: "Traffic Violations Committed By Violators",
            },
          }
      });
    },
  });
}

load_data_custom(0,0);
$("#yearsection").on("change", function () {

  if($("#yearsection option:selected").val()==0){
    
    $(".custom-filter-1").hide();
    $(".custom-filter-2").hide();
    load_data_custom(0,0);
    
  }else if($("#yearsection option:selected").val()==1){

    $(".custom-filter-1").show();
    $(".custom-filter-2").hide();
    load_data_custom($("#yearlist option:selected").val(),$("#monthlist option:selected").val());
  }
  else if($("#yearsection option:selected").val()==2){

    $(".custom-filter-1").hide();
    $(".custom-filter-2").hide();
    var d1 = new Date();
    var d2 = new Date();
    load_data_range(moment(d1).format('yyyy-MM-DD'),moment(d2).format('yyyy-MM-DD'));
  }
  else if($("#yearsection option:selected").val()==3){

    $(".custom-filter-1").hide();
    $(".custom-filter-2").hide();
    var curr = new Date; // get current date
    var first = curr.getDate() - curr.getDay(); 
    var last = first + 6;

    var firstday = new Date(curr.setDate(first+1)).toUTCString();
    var lastday = new Date(curr.setDate(last+1)).toUTCString();
    load_data_range(moment(firstday).format('yyyy-MM-DD'),moment(lastday).format('yyyy-MM-DD'));
  }
  else if($("#yearsection option:selected").val()==4){
    $(".custom-filter-1").hide();
    $(".custom-filter-2").hide();
    const d = new Date();
    load_data_custom(d.getFullYear(),d.getMonth()+1);
  }
  else if($("#yearsection option:selected").val()==5){
    $(".custom-filter-1").hide();
    $(".custom-filter-2").show();
    $(".pie-container").hide();
    $(".no-data").show();
  }

});

$("#yearlist").on("change", function () {
  load_data_custom($("#yearlist option:selected").val(),$("#monthlist option:selected").val());
});

$("#monthlist").on("change", function () {
  load_data_custom($("#yearlist option:selected").val(),$("#monthlist option:selected").val());
});
// End of Pie Chart
function load_data_range(range1,range2){
  $.ajax({
    url: "/dashboard-custom-date-range/"+range1+"/"+range2,
    success: function (data) {

      if(data.data.length==0){
        $(".pie-container").hide();
        $(".no-data").show();
      }else{
        $(".pie-container").show();
        $(".no-data").hide();
      }

      var context = $ctxP[0].getContext("2d");
      var coloR = [];

      var dynamicColors = function() {
        var r = Math.floor(Math.random() * 255);
        var g = Math.floor(Math.random() * 255);
        var b = Math.floor(Math.random() * 255);
        return "rgba(" + r + "," + g + "," + b + ",0.8)";
    };

      for (var i in data.data) {
        coloR.push(dynamicColors());
      }

      if (pieChart) {
        pieChart.destroy();
      }
      pieChart = new Chart(context, {
        type: 'pie',
          data: {
            labels: data.labels,
            datasets: [{
              data: data.data,
              backgroundColor: coloR,
              hoverBackgroundColor: coloR,
            }]
          },
          options: {
            responsive: true,
            title: {
              display: true,
              text: "Traffic Violations Committed By Violators",
            },
          }
      });
    },
  });
}

//To filter custom date
var formatYmd = date => date.toISOString().slice(0, 10);
$("#date_one").pickadate({
  selectYears: 200,
  format:"mmmm dd, yyyy",
  onSet: function(context) {
    if(($("#date_one").val().length!=0) && ($("#date_two").val().length!=0)){
      load_data_range(formatYmd(new Date($("#date_one").val())),formatYmd(new Date($("#date_two").val())));
    }
  }
});

$("#date_two").pickadate({
  selectYears: 200,
  format:"mmmm dd, yyyy",
  onSet: function(context) {
    if(($("#date_one").val().length!=0) && ($("#date_two").val().length!=0)){
      load_data_range(formatYmd(new Date($("#date_one").val())),formatYmd(new Date($("#date_two").val())));
    }
  }
});