function displayEditPopUp(index, product_name, price, quantity) {
    const popup = document.createElement('div');
    popup.id = 'popup';
    popup.classList.add('popup');

    // Create the heading element
    const heading = document.createElement('h1');
    heading.textContent = 'Edit Record';
    popup.appendChild(heading);

    // Create the form element
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = `/edit/${index}`; // Use the index directly in the action attribute

    // Create and configure input elements
    const productNameInput = document.createElement('input');
    productNameInput.type = 'text';
    productNameInput.name = 'product_name';
    productNameInput.value = product_name;

    const priceInput = document.createElement('input');
    priceInput.type = 'text';
    priceInput.name = 'price';
    priceInput.value = price;

    const quantityInput = document.createElement('input');
    quantityInput.type = 'text';
    quantityInput.name = 'quantity';
    quantityInput.value = quantity;

    const save = document.createElement('input');
    save.type = 'submit';

    const cancel = document.createElement('button');
    cancel.onclick = closePopUp;
    cancel.innerText = 'Cancel';


    // Append input elements to the form
    form.appendChild(productNameInput);
    form.appendChild(document.createElement('br'));
    form.appendChild(priceInput);
    form.appendChild(document.createElement('br'));
    form.appendChild(quantityInput);
    form.appendChild(document.createElement('br'));
    form.appendChild(save);

    // Append the form to the popup
    popup.appendChild(form);
    popup.appendChild(cancel)

    // Append the popup to the body
    document.body.appendChild(popup);

    console.log("popup", product_name, price, quantity);

}

function closePopUp() {
    console.log('cancel');
    const popup = document.getElementById('popup');
    if (popup) {
        popup.remove();
    }
}


function deleteRecord(index) {
    const popup = document.createElement('div');
    popup.id = 'popup';
    popup.classList.add('popup');
    popup.classList.add('delete-popup');

    const form = document.createElement('form');
    form.method = 'POST';
    form.action = `/delete/${index}`;

    const heading = document.createElement('h4');
    heading.textContent = `Do you want to Delete Record: ${index}`;

    const yes = document.createElement('input');
    yes.type = 'submit';
    yes.value = 'Yes';

    const No = document.createElement('button');
    No.onclick = closePopUp;
    No.innerText = 'No';

    form.appendChild(heading);
    form.appendChild(document.createElement('br'));
    form.appendChild(yes);
    form.appendChild(No);

    popup.appendChild(form);
    document.body.appendChild(popup);
}
