let nr = prompt("Voer hier een nummer in:")
nr = parseInt(nr) + 1
let antwoord = "";
for(let x = 1; x < nr; x++){
    console.log(`loop: ${x}`)
    for(let i = 0; i < x; i++){
        if(i < 1){
            antwoord = antwoord + `${i + 1}`
        }
        else{
            antwoord = antwoord + `-${i + 1}`
        }
    }
    antwoord = antwoord + "\n"
}
nr = nr - 2
for(let x = nr; x > 0; x--){
    console.log(`loop-: ${x}`)
    for(let i = 0; i < x; i++){
        if(i < 1){
            antwoord = antwoord + `${i + 1}`
        }
        else{
            antwoord = antwoord + `-${i + 1}`
        }
    }
    antwoord = antwoord + "\n"
}
document.getElementById("antwoord").innerText = antwoord;