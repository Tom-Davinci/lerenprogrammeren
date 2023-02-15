var input = document.getElementById("input");
var messages = document.getElementById("messages");
var ul = document.getElementById("list")

function inputchanged(event){
    const drinks = [];
    console.log("Changed");
    var newValue = event.target.value;
    console.log(newValue);
    if(newValue == "bier" || newValue == "fris" || newValue == "wijn"){
        messages.innerHTML = "Drankje herken ik niet!";
        setTimeout(clearmessage, 2000);
    }
    else{
        console.log(drinks.includes(newValue) == false);
        console.log(drinks);
        if(drinks.includes(newValue) == false){
        addli(newValue);
        drinks.push(newValue);
        }
        else{
            messages.innerHTML = "Dat drankje had ik al!";
            setTimeout(clearmessage, 2000);
        }
    }
    clearinput();
}

function addli(drink){
    var li = document.createElement("li")
    li.appendChild(document.createTextNode(drink));
    ul.appendChild(li);
}

function clearmessage(){
    messages.innerHTML = "";
}

function clearinput(){
    input.value = "";
}

input.onchange = inputchanged;