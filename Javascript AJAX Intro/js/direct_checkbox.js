/**
* Created by TheOneTAR on 8/26/15.
*/

var inventory = document.getElementById('inventory');
var woodstock, material, price;

function Product(name, stock, price) {
    this.checked = false;
    this.name = name;
    this.stock = stock;
    this.price = price;

    this.adjustStock = function(num) {
        this.stock -= num;
    };

    this.inStock = function () {
        return this.stock > 0;
    };
}

var materials = [];

function populateInventoryDOM() {
    // Loop through materials
    // Add a row for each item in materials into the inventory
    // Make sure that stock class reflects inStock
    // Make sure that checkbox status reflects checked
    for (var i=0; i < materials.length; i++) {
        var newProdRow = document.createElement('tr');

        // Checkbox column
        var checkboxCell = document.createElement('td');
        var checkbox = document.createElement('input');
        checkbox.type = "checkbox";
        checkbox.checked = materials[i].checked;
        checkboxCell.appendChild(checkbox);
        newProdRow.appendChild(checkboxCell);

        // Name Column
        var nameCol = document.createElement('td');
        var nameText = document.createTextNode(materials[i].name);
        nameCol.appendChild(nameText);
        newProdRow.appendChild(nameCol);

        // Price Column
        var priceCol = document.createElement('td');
        var priceText = document.createTextNode('$' + materials[i].price);
        priceCol.appendChild(priceText);
        newProdRow.appendChild(priceCol);

        // Stock Column
        var stockCol = document.createElement('td');
        stockCol.className = materials[i].inStock();
        var stockText = document.createTextNode(materials[i].stock);
        stockCol.appendChild(stockText);
        newProdRow.appendChild(stockCol);

        inventory.appendChild(newProdRow);
    }

}

function checkAllHandler(e, number) {
    console.log(e);
    var inputs = inventory.getElementsByTagName('input');
    for (var i=0; i < inputs.length; i++) {
        if (inputs[i].type == 'checkbox') {
            inputs[i].checked = e.target.checked;
        }
    }
}
checkAll = document.getElementById('checkAll');
checkAll.addEventListener('click', function (e) {
    checkAllHandler(e, 6);
}, false);

function removeStock() {
    var rows = inventory.getElementsByTagName('tr');
    for (var i=0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs.length > 0 ) {
            if (inputs[0].type == 'checkbox') {
                if (inputs[0].checked) {
                    // Flip the status of the stock column
                    var stock = rows[i].lastElementChild;
                    stock.className = 'false';
                }
            }
        }
    }
}

function addStock() {
    var rows = inventory.getElementsByTagName('tr');

    for (var i=0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type == 'checkbox') {
            if (inputs[0].checked) {
                // Flip the status of the stock column
                var stock = rows[i].lastElementChild;
                stock.className = 'true';
            }
        }
    }
}

function addNewStock() {
    material = document.getElementById('material').value;
    price = document.getElementById('price').value;

    if (material === '' || price === '' || isNaN(price)) {
        return
    }

    var newProdRow = document.createElement('tr');

    // Checkbox column
    var checkboxCell = document.createElement('td');
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.checked = false;
    checkboxCell.appendChild(checkbox);
    newProdRow.appendChild(checkboxCell);

    // Name Column
    var nameCol = document.createElement('td');
    var nameText = document.createTextNode(material);
    nameCol.appendChild(nameText);
    newProdRow.appendChild(nameCol);

    // Price Column
    var priceCol = document.createElement('td');
    var priceText = document.createTextNode('$' + price);
    priceCol.appendChild(priceText);
    newProdRow.appendChild(priceCol);

    // Stock Column
    var stockCol = document.createElement('td');
    stockCol.className = 'true';
    var stockText = document.createTextNode('10');
    stockCol.appendChild(stockText);
    newProdRow.appendChild(stockCol);

    inventory.appendChild(newProdRow);
    materials.push(new Product(material, 10, price));

    //var newRow = '<tr>';
    //newRow += '<td><input type="checkbox"/></td>';
    //newRow += '<td>' + material + '</td>';
    //newRow += '<td>$' + price + '</td>';
    //newRow += '<td class="false">No</td>';
    //newRow += '</tr>';

    //inventory.innerHTML += newRow;

    document.getElementById('material').value = '';
    document.getElementById('price').value = '';
}


// Make an AJAX call to get the data from the server
var newRequest = new XMLHttpRequest();

newRequest.onload = function () {
    if (newRequest.status === 200) {
        var response = newRequest.responseXML;
        var items = response.getElementsByTagName('item');

        for (var i=0; i< items.length; i++) {
            // Loop through item list and add items
            var product = new Product(
                items[i].getAttribute('name'),
                items[i].getElementsByTagName('numInStock')[0].textContent,
                items[i].getAttribute('price'));
            materials.push(product);
        }

        populateInventoryDOM();

    }
};

newRequest.open('GET','data/stock.xml', true);
newRequest.send(null);

// Get the JSON stuff
var otherRequest = new XMLHttpRequest();

otherRequest.onload = function () {
    if (otherRequest.status === 200) {
        var responseObject = JSON.parse(otherRequest.responseText);
        var items = responseObject.inventory.item;

        // Loop through the returned list, creating & adding Products
        for (var i = 0; i < items.length; i++) {
            var product = new Product(
                items[i].name,
                items[i].numInStock,
                items[i].price
            );
            materials.push(product);
        }

        // Populate #inventory using the materials list
        populateInventoryDOM();
    }

};

otherRequest.open("GET", "data/stock.json", true);
otherRequest.send(null);