var settledateinput = document.getElementById('settle_before').value
var datenow = new Date();
var settlebefore = new Date(Date.parse(settledateinput));

if (datenow>settlebefore){
    $("#settle_status_label").addClass('active');
    $("#settle_status").addClass('red-text');
    document.getElementById('settle_status').value="Overdue";
}
else{
    $("#settle_status_label").addClass('active');
    $("#settle_status").addClass('green-text');
    document.getElementById('settle_status').value="Active";
}