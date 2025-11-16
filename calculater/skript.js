let merkit = [];
let sama = "";
let valimerkki;

function clickt(merkki) {
    
    let nayta = document.getElementById("nayta");
    
    if (merkit.length == 1 && isNaN(merkki) == false) {
        nayta.innerHTML = "";
        merkit = []
    }

    console.log(merkit)
    

    if (isNaN(merkki) == false && merkki.length > 0 || merkki == ".") {
        sama += merkki
        nayta.innerHTML += merkki;
    } else {
        merkit.push(sama);
        sama = ""
    }
    
    let sisaltaako = merkit.includes(merkki, 1) 
    
    if (isNaN(merkki) == true && merkki.length > 0  && merkki != "=" && merkki != "." && sisaltaako == false) {
        merkit.push(merkki);   
        nayta.innerHTML += " " + merkki + " ";
    }

    if (merkki == "c"){
        nayta.innerHTML = ""
        merkit = []
    }
    
    let vastaus;


    let filter_merkit = merkit.filter(function (e) {
        return e; // Katsoo ettei ole tyhjiä merkkejä arrayssä
    })

    merkit = filter_merkit

    for (let x = 0; x < merkit.length; x++) {
       
        valimerkki = merkit[1]
        
        
        if (merkit[x] == "="){
            return;
        }

        if (isNaN(merkit[0]) || isNaN(merkit[2])) {
            continue;
        } else {

            if (merkit[1] != merkki) {
                valimerkki = merkit[1] 
            }
           
            switch(valimerkki) {
                case "+":
                    vastaus = parseFloat(merkit[0]) + parseFloat(merkit[2])
                    nayta.innerHTML = `${parseFloat(merkit[0])} + ${parseFloat(merkit[2])} = ${vastaus}`;
                    merkit = []
                    merkit.push(`${vastaus}`)                      
                    break;
                case "-":
                    vastaus = parseFloat(merkit[0]) - parseFloat(merkit[2])
                    nayta.innerHTML = `${parseFloat(merkit[0])} - ${parseFloat(merkit[2])} = ${vastaus}`;
                    merkit = []
                    merkit.push(`${vastaus}`)                        
                    break;
                case "*":
                    vastaus = parseFloat(merkit[0]) * parseFloat(merkit[2])
                    nayta.innerHTML = `${parseFloat(merkit[0])} * ${parseFloat(merkit[2])} = ${vastaus}`;
                    merkit = []
                    merkit.push(`${vastaus}`)                        
                    break;
                case "/":
                    vastaus = parseFloat(merkit[0]) / parseFloat(merkit[2])
                    nayta.innerHTML = `${parseFloat(merkit[0])} / ${parseFloat(merkit[2])} = ${vastaus}`;
                    merkit = []
                    merkit.push(`${vastaus}`)                        
                    break;
            }
        }
    }
}
