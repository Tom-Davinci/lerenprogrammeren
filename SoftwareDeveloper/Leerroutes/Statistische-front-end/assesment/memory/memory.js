function shuffle(array){
    let currentIndex = array.length, randomIndex;
    while (currentIndex != 0){
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex --;
        [array[currentIndex], array[randomIndex] = array[randomIndex], array[currentIndex]];
    }
    return array;
}

var images1 = document.getElementById("images1");
var images2 = document.getElementById("images2");

var numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
