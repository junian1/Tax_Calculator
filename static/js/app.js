// const monthlysalary = document.getElementById('uiMonthlySalary')
// const bonus = document.getElementById('uiBonus')
// const donations = document.getElementById('uiDonations')
// const deductibles = document.getElementById('uiDeductibles')
// const epf_perc = getEPFPercentage()
// const estTax = document.getElementById("uiEstimatedTax")
// const error = document.getElementById("error")


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
  var bonus = document.getElementById("uiBonus");
  var donations = document.getElementById("uiDonations");
  var deductibles = document.getElementById("uiDeductibles");
  var epf_perc = getEPFPercentage();
  var estTax = document.getElementById("uiEstimatedTax");
  //var url = "http://127.0.0.1:5000/income_tax"; // use this for localhost
  var url = "https://incometax-calculator.herokuapp.com/income_tax"; 

  $.post(url, {
      monthlysalary: parseFloat(monthlysalary.value),
      bonus: parseFloat(bonus.value),
      donations: parseFloat(donations.value),
      deductibles: parseFloat(deductibles.value),
      epf_perc: epf_perc
  },function(data, status) {
      console.log(data.estimated_tax);
      estTax.innerHTML = "<h2>RM " + data.estimated_tax.toString() + "</h2>";
      console.log(status);
  });
}



// function isnumeric(inputtxt) {
	// var numbers = /^[0-9]+$/;
	// if(inputtxt.value.match(numbers)) {
		// alert('Your value is valid');
		// document.form.text.focus();
		// return true;
	// }
	// else {
		// alert('Your value is not valid');
		// document.form.text.focus();
		// return false;
	// }
// }

