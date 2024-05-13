buttonAmount = 30;
for(let x = 1; x < buttonAmount + 1; x++) {
    document.body.onload = addElement(x);
}

function addElement(num){
    const newButton = document.createElement("BUTTON");
    const text = document.createTextNode(num);

    newButton.appendChild(text);
    newButton.onclick = function() {buttonClicked(newButton)};
    newButton.style.backgroundColor = "green";

    const container = document.getElementById("container");
    container.appendChild(newButton);

    document.body.insertBefore(container, newButton.nextSibling);
}

function buttonClicked(button) {
    button.style.backgroundColor = "red";
}