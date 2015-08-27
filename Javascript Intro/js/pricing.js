/**
* Created by TheOneTAR on 8/25/15.
*/
var inventory = document.getElementById('inventory');
var woodstock, material, price;

checkAll = document.getElementById('checkAll');
console.log(checkAll);
checkAll.onclick = checkAllHandler(checkAll);

function updateMainCheckbox(checkbox) {
    if (!checkbox.checked) {
        document.getElementById('checkAll').checked = false;
    }
}

function checkAllHandler(check) {
    var inputs = inventory.getElementsByTagName('input');
    for (var i=0; i < inputs.length; i++) {
        if (inputs[i].type == 'checkbox') {
            inputs[i].checked = true;
        }
    }
}

function removeStock() {
    var rows = inventory.getElementsByTagName('tr');
    for (var i=0; i < rows.length; i++) {
        var input = rows[i].getElementsByTagName('input');
        if (input[0].type == 'checkbox') {
            if (input[0].checked) {
                rows[i].lastElementChild.className = "false";
                rows[i].lastElementChild.textContent = "No";
            }
        }
    }
};

function addStock() {
    var rows = inventory.getElementsByTagName('tr');
    for (var i=0; i < rows.length; i++) {
        var input = rows[i].getElementsByTagName('input');
        if (input[0].type == 'checkbox') {
            if (input[0].checked) {
                rows[i].lastElementChild.className = "true";
                rows[i].lastElementChild.textContent = "Yes";
            }
        }
    }
};

function addNewStock() {
    material = document.getElementById('material').value;
    price = document.getElementById('price').value;

    if (material === '' || price === '' || isNaN(price)) {
        return
    }

    var newRow = "<tr>";
    newRow += '<td><input type="checkbox" onclick="updateMainCheckbox(this)"/></td>';
    newRow += '<td>' + material + '</td>';
    newRow += '<td>$' + price + '</td>';
    newRow += '<td class="false">No</td>';
    newRow += '</tr>';

    inventory.innerHTML += newRow;

    document.getElementById('material').value = '';
    document.getElementById('price').value = '';
};