function getEPFPercentage() {
  var uiEPF = document.getElementsByName("uiEPF");
  for(var i in uiEPF) {
    if(uiEPF[i].checked) {
      return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}


function OnClickedEstimateTax() {
  console.log("Estimate income tax clicked");
  var monthlysalary = document.getElementById("uiMonthlySalary");
  var donations = document.getElementById("uiDonations");
  var deductibles = document.getElementById("uiDeductibles");
  var epf_perc = getEPFPercentage();
  var estTax = document.getElementById("uiEstimatedTax");

  var url = "http://127.0.0.1:5000/income_tax"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/income_tax"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      monthlysalary: parseFloat(monthlysalary.value),
      donations: parseFloat(donations.value),
      deductibles: parseFloat(deductibles.value),
      epf_perc: epf_perc
  },function(data, status) {
      console.log(data.estimated_tax);
      estTax.innerHTML = "<h2>RM " + data.estimated_tax.toString() + "</h2>";
      console.log(status);
  });
}


function onPageLoad() {
  console.log( "document loaded" );
  // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;