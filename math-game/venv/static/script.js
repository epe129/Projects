let laskuNäytä = document.getElementById("lasku");
let merkit = ["+","-","/","*"]
let vastaus = 0;
let ekaNumero = Math.floor(Math.random() * 10) + 1;
let tokaNumero = Math.floor(Math.random() * 10) + 1;
let randomMerkki = Math.floor(Math.random() * merkit.length);
let merkki = merkit[randomMerkki];
    
laskuNäytä.innerHTML = `Lasku: ${ekaNumero} ${merkki} ${tokaNumero}`

function naytaVastaus() {

    const v = document.getElementById("vastaus");
    const n = document.getElementById("Onko");
    
    const inputShow = v.value

    switch(merkki) {
        case "+":
            vastaus = ekaNumero + tokaNumero;
            break;
        case "-":
            vastaus = ekaNumero - tokaNumero;
            break;
        case "/":
            vastaus = ekaNumero / tokaNumero;
            break;       
        case "*":
            vastaus = ekaNumero * tokaNumero;
            break;
        }

    if (parseFloat(inputShow) == parseFloat(vastaus)) {
        n.innerHTML = "Oikein: " + vastaus;
    } else {
        console.log(vastaus)
        n.innerHTML = "Väärin: " + vastaus;
    }
}
    

