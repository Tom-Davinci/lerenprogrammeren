document.body.onload = addElement("green");
document.body.onload = addElement("red");
document.body.onload = addElement("blue");

function addElement(color) {
    const newButton = document.createElement("BUTTON");
    const text = document.createTextNode(color)

    newButton.appendChild(text);
    newButton.onclick = function() {buttonClicked(color)};
    newButton.style.backgroundColor = color;

    const container = document.getElementById("container");
    container.appendChild(newButton);

    document.body.insertBefore(container, newButton.nextSibling)
}

function buttonClicked(color) {
    document.body.style.backgroundColor = color;
}