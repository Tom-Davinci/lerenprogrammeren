function fibonacci() {
    n1 = 0
    n2 = 1
    fibo = "0\n 1\n"
    for(var i = 0; i < 19; i++) {
        nextNum = n1 + n2
        n1 = n2
        n2 = nextNum
        fibo += nextNum + "\n"
    }
    return fibo
}


document.getElementById("fibonacci").innerText = fibonacci()