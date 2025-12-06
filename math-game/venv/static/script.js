let laskuNäytä = document.getElementById("lasku");
let merkit = ["+","-","/","*"]
let vastaus = [];

let ekaNumero = Math.floor(Math.random() * 10) + 1;
let tokaNumero = Math.floor(Math.random() * 10) + 1;
let kolmasNumero = Math.floor(Math.random() * 10) + 1;

let randomMerkki = Math.floor(Math.random() * merkit.length);
let randomMerkki2 = Math.floor(Math.random() * merkit.length);

let merkki = merkit[randomMerkki];

let merkki2 = merkit[randomMerkki2];

laskuNäytä.innerHTML = `Lasku: ${ekaNumero} ${merkki} ${tokaNumero} ${merkki2} ${kolmasNumero}`

vastaus.push(ekaNumero)
    
vastaus.push(merkki)
    
vastaus.push(tokaNumero)

vastaus.push(merkki2)

vastaus.push(kolmasNumero)


let v = document.getElementById("vastaus");
let n = document.getElementById("Onko");
    

let etsiKertomerkki;
let etsiJakomerkki;
let merkkiIndex;
let tulos = 0;

function naytaVastaus() {
    let inputShow = v.value

    for (let i = 0; i < vastaus.length; i++) {    
        
        etsiJakomerkki = vastaus.includes("/")        
        etsiKertomerkki = vastaus.includes("*")
       
        if (etsiJakomerkki == true || etsiKertomerkki == true) {
            switch(vastaus[i]) {
                case "/":
                    merkkiIndex = vastaus.indexOf("/")

                    tulos = vastaus[merkkiIndex-1] / vastaus[merkkiIndex+1];
                    
                    console.log(vastaus[merkkiIndex-1] , vastaus[merkkiIndex+1])
                    
                    vastaus.splice(merkkiIndex-1, merkkiIndex+2, tulos);
                        
                    console.log(vastaus)

                    i = 0;
                    tulos = 0
                    merkkiIndex = 0

                    etsiJakomerkki = vastaus.includes("/")

                    break;       
                case "*":
                    merkkiIndex = vastaus.indexOf("*")
                        
                    tulos = vastaus[merkkiIndex-1] * vastaus[merkkiIndex+1];
                        
                    vastaus.splice(merkkiIndex-1, merkkiIndex+2, tulos);
                        
                    console.log(vastaus)
                        
                    i = 0;
                    tulos = 0
                    merkkiIndex = 0
                    etsiKertomerkki = vastaus.includes("*")

                    break;
                }
            } else {
                switch(vastaus[i]) {
                    case "+":
                        merkkiIndex = vastaus.indexOf("+")
                            
                        tulos = vastaus[merkkiIndex-1] + vastaus[merkkiIndex+1];
                            
                        vastaus.splice(merkkiIndex-1, merkkiIndex+2, tulos);
                            
                        console.log(vastaus)
                            
                        i--;
                        tulos = 0
                        merkkiIndex = 0
                            
                        break;
                    case "-":
                        merkkiIndex = vastaus.indexOf("-")
                            
                        tulos = vastaus[merkkiIndex-1] - vastaus[merkkiIndex+1];
                            
                        vastaus.splice(merkkiIndex-1, merkkiIndex+2, tulos);
                            
                        console.log(vastaus)
                            
                        i--;
                        tulos = 0
                        merkkiIndex = 0
                            
                        break;
                    }
                }
    }

    if (parseFloat(inputShow) == parseFloat(vastaus[0])) {
        n.innerHTML = "Oikein: " + vastaus[0];
    } else {
        console.log(vastaus)
        n.innerHTML = "Väärin: " + vastaus[0];
    }

}
    

