const foodBalanceWrapper = document.getElementById("foodBalanceWrapper")
foodBalanceWrapper.style.display = "none";

// provided: vanilla JS autocomplete
// https://goodies.pixabay.com/javascript/auto-complete/demo.html
new autoComplete({
  selector: 'input[name="foodPicker"]',
  minChars: 2,
  source: function(term, suggest){
    term = term.toLowerCase();
    let choices = Object.keys(foodDb);  // defined in food.js
    let matches = [];
    for(i=0; i<choices.length; i++){
      let kcal = foodDb[choices[i]];
      if(kcal == 0){
        continue;
      }

      if(~choices[i].toLowerCase().indexOf(term)){
        let item = `${choices[i]} (${kcal} kcal)`;
        matches.push(item);
      }
    }
    suggest(matches);
  }
});


// provided: handle form submission to not do it as inline JS
// https://stackoverflow.com/a/5384732
function processForm(e) {
    if (e.preventDefault) e.preventDefault();
    updateFoodLog();
    return false;
}
var form = document.getElementById('foodPickerForm');
if (form.attachEvent) {
    form.attachEvent("submit", processForm);
} else {
    form.addEventListener("submit", processForm);
}


// helpers
function recalculateTotal(){
  // get all table cells (tds) and sum the calories = td with kcal
  var result = 0;
  var ftable = document.getElementById("foodBalanceTable");
  console.log("aaaa")
  
  d = ftable.getElementsByTagName("tr").length
  for(var i = 1; i < d; i++){
    row = ftable.getElementsByTagName("tr")[i];
    cals = row.getElementsByTagName("td")[1].innerHTML;
    result += parseFloat(cals);
  }
  return result;
}

function updateTotalKcal(tres){
  // write the total kcal count into  the total id, if 0 hide the
  // foodBalanceWrapper div
  total = document.getElementById("total");
  total.innerHTML = tres;
}

function emptyFoodPicker(){
  // reset the foodPicker ID value
}

function removeRow(){
  // remove a table row and update the total kcal
  // https://stackoverflow.com/a/53085148
  var td = event.target.parentNode; 
  var tr = td.parentNode; // the row to be removed
  tr.parentNode.removeChild(tr);

  result = recalculateTotal();
  updateTotalKcal(result);
}

function updateFoodLog(){
  // udate the food table with the new food, building up the inner dom
  // elements, including adding a delete button / onclick handler
  // finally call updateTotalKcal and emptyFoodPicker

  var selectedfood = document.getElementById("foodPicker").value;
  var mySubString = selectedfood.substring(
    selectedfood.lastIndexOf("(") + 1, 
    selectedfood.lastIndexOf(" ")
  );
  var tableRef = document.getElementById('foodBalanceTable').getElementsByTagName('tbody')[0];
  var newRow   = tableRef.insertRow();

  var newCell  = newRow.insertCell(0);
  newCell.innerHTML = '<input type="button" value="X" onclick="removeRow()">  '+ selectedfood;
  var newCell2 = newRow.insertCell(1);
  newCell2.innerHTML = mySubString;



  result = recalculateTotal();
  updateTotalKcal(result);
  
}
