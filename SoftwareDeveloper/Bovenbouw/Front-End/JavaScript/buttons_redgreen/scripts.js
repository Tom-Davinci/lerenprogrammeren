buttonAmount = 30;
for(let x = 1; x < buttonAmount + 1; x++) {
    document.body.onload = addElement(x);
}

function addElement(num){
    const newButton = document.createElement("BUTTON");
    const text = document.createTextNode(num);

    newButton.setAttribute("id", "b" + num)
    localStorage.setItem(newButton.id, "0")
    newButton.appendChild(text);
    newButton.onclick = function() {buttonClicked(newButton)};
    newButton.style.backgroundColor = "green";

    const container = document.getElementById("container");
    container.appendChild(newButton);

    document.body.insertBefore(container, newButton.nextSibling);
}

function buttonClicked(button) {
    setColour(button, localStorage.getItem(button.id))
    let buttonCounter = localStorage.getItem(button.id);
    buttonCounter = parseInt(buttonCounter) + 1;
    localStorage.setItem(button.id, buttonCounter);
}

function setColour(button, num) {
    button.style.backgroundColor = "red";
    if(num > 0) {
        button.style.backgroundColor = "purple";
    }
    if(num > 1) {
        button.style.backgroundColor = "blue";
    }
    if(num > 2) {
        button.style.backgroundColor = "zwart";
    }
    if(num > 3) {
        button.remove();
    }
}