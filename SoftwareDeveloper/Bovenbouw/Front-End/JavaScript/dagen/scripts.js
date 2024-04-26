const dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"];

function dagenGetter(dagen, start, end, reverse) {
    let returnValue = "";
    if(reverse == true) {
        for(let i = start; end < i; i--) {
            returnValue += dagen[i] + ", ";
         }
    }
    else{
        for(let i = start; i < end; i++) {
           returnValue += dagen[i] + ", ";
        }
    }
    return returnValue;
}

document.getElementById("dagen").innerText = dagenGetter(dagen, 0, 7, false);
document.getElementById("werkdagen").innerText = dagenGetter(dagen, 0, 5, false);
document.getElementById("weekenddagen").innerText = dagenGetter(dagen, 5, 7, false);
document.getElementById("omgekeerd").innerText = dagenGetter(dagen, 6, -1, true);
document.getElementById("werkdagen-omgekeerd").innerText = dagenGetter(dagen, 4, -1, true);
document.getElementById("weekend-omgekeerd").innerText = dagenGetter(dagen, 6, 4, true);