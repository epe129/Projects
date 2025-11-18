let vastaus = 0
let merkit = []
let vastaukset = []
let sama = "";
let index = 0;
let a = "";
let b = "";
let suoritettu = false

function clickt(merkki) { 
    let nayta = document.getElementById("nayta");

    if (isNaN(merkki) == false && merkki.length > 0 || merkki == ".") {
        if (merkit.length == 1) {
            merkit[0] += merkki
        } else {
            sama += merkki
        }
        nayta.innerHTML += merkki;
    } else {
        merkit.push(sama);
        sama = ""
    }

    if (isNaN(merkki) == true && merkki.length > 0 && merkki != ".") {
        merkit.push(merkki);   
        nayta.innerHTML += " " + merkki + " ";
    }

    if (merkki == "c"){
        nayta.innerHTML = "" 
        merkit = []
        vastaus = 0 
    }
    
    let filter_merkit = merkit.filter(function (e) {
        return e; 
    })

    merkit = filter_merkit

    let siKerto = merkit.includes("*");
    let siJako = merkit.includes("/");

    if (merkki == "="){
        console.log("menee")
        for (let i = 0; i < merkit.length; i++) {
            siKerto = merkit.includes("*");
            siJako = merkit.includes("/");
            
            if (merkit[i] == "*" || merkit[i] == "/" && siKerto == true || siJako == true) {
                switch(merkit[i]) {
                    case "*":
                        index = i
                        indexMerkki = merkit.indexOf(merkit[i])
                        a = parseFloat(merkit[index-1])
                        b = parseFloat(merkit[index+1])
                        v = a * b   
                        vastaus += v
                        if (vastaus == 0) {
                            merkit.splice(indexMerkki-1, 3, "0");
                        } else {
                            merkit.splice(indexMerkki-1, 3, v);
                        }
                        console.log(merkit)                                         
                        if(merkit[1] == "=") {
                            merkit.splice(1, 1);
                        }
                        suoritettu = true
                        
                        i = 0
                        break;
                    case "/":
                        index = i
                        indexMerkki = merkit.indexOf(merkit[i])
                        a = parseFloat(merkit[index-1])
                        b = parseFloat(merkit[index+1])
                        v = a / b                    
                        vastaus += v

                        if (vastaus == 0) {
                            merkit.splice(indexMerkki-1, 3, "0");
                        } else {
                            merkit.splice(indexMerkki-1, 3, v);
                        }

                        if(merkit[1] == "=") {
                            merkit.splice(1, 1);
                        }
                        suoritettu = true
                       
                        i = 0
                        break;
                }
            } else if (siJako == false && siKerto == false) {
                switch(merkit[i]) {
                    case "+":
                        console.log("moi")
                        index = i
                        indexMerkki = merkit.indexOf(merkit[i])
                        a = parseFloat(merkit[index-1])
                        b = parseFloat(merkit[index+1])
                        v = a + b
                        vastaus += v
                        
                        if (vastaus == 0) {
                            merkit.splice(indexMerkki-1, 3, "0");
                        } else {
                            merkit.splice(indexMerkki-1, 3, v);
                        }
                        
                        if(merkit[1] == "=") {
                            merkit.splice(1, 1);
                        }
                        i--; 
                        break;
                    case "-":
                        index = i
                        indexMerkki = merkit.indexOf(merkit[i])
                        a = parseFloat(merkit[index-1])
                        b = parseFloat(merkit[index+1])
                        v = a - b
                        vastaus += v
                        if (vastaus == 0) {
                            merkit.splice(indexMerkki-1, 3, "0");
                        } else {
                            merkit.splice(indexMerkki-1, 3, v);
                        }

                        if(merkit[1] == "=") {
                            merkit.splice(1, 1);
                        }
                        i--; 
                        break;
                    }
                }
            }   
    } 
    if (merkki == "=") {
        nayta.innerHTML += merkit[0]
        vastaus = 0 
        i = 0
        suoritettu = false
    }
}

