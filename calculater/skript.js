let vastaus = 0
let merkit = []
let vastaukset = []
let sama = "";
let index = 0;
let a = "";
let b = "";

function clickt(merkki) { 
    let nayta = document.getElementById("nayta");

    if (isNaN(merkki) == false && merkki.length > 0 ) {
        sama += merkki
        nayta.innerHTML += merkki;
    } else {
        merkit.push(sama);
        sama = ""
    }

    if (isNaN(merkki) == true && merkki.length > 0 ) {
        merkit.push(merkki);   
        nayta.innerHTML += " " + merkki + " ";
    }

    if (merkki == "c"){
        nayta.innerHTML = "" 
    }
    
    let filter_merkit = merkit.filter(function (e) {
        return e; 
    })

    merkit = filter_merkit
    console.log(merkit) 
    
    if (merkki == "="){
        for (let i = 0; i < merkit.length; i++) {
            switch(merkit[i]) {
                case "*":
                    index = i
                    a = parseFloat(merkit[index-1])
                    b = parseFloat(merkit[index+1])
                    v = a * b   
                    vastaus += v
                    // merkit.splice(index-1, 3, v);                                         
                    // console.log(merkit)
                    // i--; 
                    break;
                case "/":
                    index = i
                    a = parseFloat(merkit[index-1])
                    b = parseFloat(merkit[index+1])
                    v = a / b                    
                    vastaus += v

                    // merkit.splice(index-1, 3, v); 
                    // console.log(merkit)
                    // i--; 
                    break;
                case "+":
                    index = i
                    a = parseFloat(merkit[index-1])
                    b = parseFloat(merkit[index+1])
                    v = a + b
                    vastaus += v

                    // merkit.splice(index-1, 3, v); 
                    // console.log(merkit)
                    // i--; 
                    break;
                case "-":
                    index = i
                    a = parseFloat(merkit[index-1])
                    b = parseFloat(merkit[index+1])
                    v = a - b
                    vastaus += v

                    // merkit.splice(index-1, 3, v); 
                    // console.log(merkit)
                    // i--; 
                    break;
                case "=":
                    nayta.innerHTML += vastaus 
                    merkit = [] 
                    merkit.push(vastaus) 
                    vastaus = 0 
                    break;
            }
        }   
    }
}

//                     merkit = []
                    // merkit.push(vastaus)
                    // vastaus = 0

// vastaukset.push(v)
                    // vastaus += v
                    
// let vastaukset = []; 
// let merkit = []; 
// let sama = ""; 
// let valimerkki; 
// let vastaus; 
// let index;
// let v = 0

// function clickt(merkki) { 
//     let nayta = document.getElementById("nayta");

//     if (isNaN(merkki) == false && merkki.length > 0 || merkki == ".") {
//         sama += merkki
//         nayta.innerHTML += merkki;
//     } else {
//         merkit.push(sama);
//         sama = ""
//     }

//     if (isNaN(merkki) == true && merkki.length > 0 && merkki != ".") {
//         merkit.push(merkki);   
//         nayta.innerHTML += " " + merkki + " ";
//     }

//     if (merkki == "c"){
//         nayta.innerHTML = ""
//         merkit = []
//         vastaukset = []
//         v = 0
//         sama = ""
//         vastaus = ""
//     }

//     let filter_merkit = merkit.filter(function (e) {
//         return e; 
//     })

//     merkit = filter_merkit


//     for (let c = 0; c < merkit.length; c++) {
//         if ("=" == merkit[c]) {
//             for (let x = 0; x < merkit.length; x++) {
//                 switch(merkit[x]) {
//                     case "*":
//                         index = merkit.indexOf(merkit[x])
//                         vastaus = parseFloat(merkit[index-1]) * parseFloat(merkit[index+1])
//                         vastaukset.push(vastaus) 
//                         v += vastaus
//                         vastaus = ""
//                         sama += vastaus                        
//                         break;
//                     case "/":
//                         index = merkit.indexOf(merkit[x])
//                         vastaus = parseFloat(merkit[index-1]) / parseFloat(merkit[index+1])
//                         vastaukset.push(vastaus) 
//                         v += vastaus
//                         vastaus = ""
//                         sama += vastaus
//                         break;
//                     case "+":
//                         index = merkit.indexOf(merkit[x])
//                         vastaus = parseFloat(merkit[index-1]) + parseFloat(merkit[index+1])
//                         vastaukset.push(vastaus) 
//                         v += vastaus
//                         vastaus = ""
//                         sama += vastaus                      
//                         break;
//                     case "-":
//                         index = merkit.indexOf(merkit[x])
//                         vastaus = parseFloat(merkit[index-1]) - parseFloat(merkit[index+1])
//                         vastaukset.push(vastaus) 
//                         v += vastaus
//                         vastaus = ""
//                         sama += vastaus                        
//                         break;
//                     case "=": 
//                         nayta.innerHTML += v;
//                         merkit = []
//                         merkit.push(v)
//                         v = 0
//                 }
//             }
//         }        
//     }
// }














//  if (merkit[x] == "*") {
//                     index = merkit.indexOf(merkit[x])
//                     if (edellinen.length == 1) {
//                         vastaus = parseFloat(edellinen[0]) * parseFloat(merkit[index+1])
//                     } else {
//                         vastaus = parseFloat(merkit[index-1]) * parseFloat(merkit[index+1])
//                     }
                    
//                     vastaukset.push(vastaus)                    
//                     edellinen.push(vastaus)
                    
//                     vastaus = ""
//                     sama += vastaus   
//                 } else if (merkit[x] == "/") {
//                     index = merkit.indexOf(merkit[x])
                    
//                     if (edellinen.length == 1) {
//                         vastaus = parseFloat(edellinen[0]) / parseFloat(merkit[index+1])
//                     } else {
//                         vastaus = parseFloat(merkit[index-1]) / parseFloat(merkit[index+1])
//                     }

//                     vastaukset.push(vastaus)                    
//                     edellinen.push(vastaus)
                    
//                     vastaus = ""
//                     sama += vastaus
//                 } else if (merkit[x] == "+") {
//                     index = merkit.indexOf(merkit[x])
                    
//                     if (edellinen.length == 1) {
//                         vastaus = parseFloat(edellinen[0]) + parseFloat(merkit[index+1])
//                     } else {
//                         vastaus = parseFloat(merkit[index-1]) + parseFloat(merkit[index+1])
//                     }
                    
//                     vastaukset.push(vastaus)                    
//                     edellinen.push(vastaus)
                    
//                     vastaus = ""
//                     sama += vastaus
//                 } else if (merkit[x] == "-") {
//                     index = merkit.indexOf(merkit[x])
                    
//                     if (edellinen.length == 1) {
//                         vastaus = parseFloat(edellinen[0]) - parseFloat(merkit[index+1])
//                     } else {
//                         vastaus = parseFloat(merkit[index-1]) - parseFloat(merkit[index+1])
//                     }
                    
//                     vastaukset.push(vastaus)                    
//                     edellinen.push(vastaus)
                    
//                     vastaus = ""
//                     sama += vastaus
//                 } else if (merkit[x] == "=") {
//                     v = 0
//                     for (let y = 0; y < vastaukset.length; y++) {
//                         v += vastaukset[y]
//                         console.log(vastaukset[y])
//                     }                    
//                     nayta.innerHTML += v;
//                 }









































































































// // defaultcase jos ei oo välimerkkiä
// let merkit = [];
// let sama = "";
// let valimerkki;

// function clickt(merkki) {
    
//     let nayta = document.getElementById("nayta");
    
//     if (merkit.length == 1 && isNaN(merkki) == false) {
//         nayta.innerHTML = "";
//         merkit = []
//     }

//     console.log(merkit)
    

//     if (isNaN(merkki) == false && merkki.length > 0 || merkki == ".") {
//         sama += merkki
//         nayta.innerHTML += merkki;
//     } else {
//         merkit.push(sama);
//         sama = ""
//     }
    
//     let sisaltaako = merkit.includes(merkki, 1) 
    
//     if (isNaN(merkki) == true && merkki.length > 0  && merkki != "=" && merkki != "." && sisaltaako == false) {
//         merkit.push(merkki);   
//         nayta.innerHTML += " " + merkki + " ";
//     }

//     if (merkki == "c"){
//         nayta.innerHTML = ""
//         merkit = []
//     }
    
//     let vastaus;


//     let filter_merkit = merkit.filter(function (e) {
//         return e; // Katsoo ettei ole tyhjiä merkkejä arrayssä
//     })

//     merkit = filter_merkit

//     for (let x = 0; x < merkit.length; x++) {
       
//         valimerkki = merkit[1]
        
        
//         if (merkit[x] == "="){
//             return;
//         }

//         if (isNaN(merkit[0]) || isNaN(merkit[2])) {
//             continue;
//         } else {

//             if (merkit[1] != merkki) {
//                 valimerkki = merkit[1] 
//             }
           
//             switch(valimerkki) {
//                 case "+":
//                     vastaus = parseFloat(merkit[0]) + parseFloat(merkit[2])
//                     nayta.innerHTML = `${parseFloat(merkit[0])} + ${parseFloat(merkit[2])} = ${vastaus}`;
//                     merkit = []
//                     merkit.push(`${vastaus}`)                      
//                     break;
//                 case "-":
//                     vastaus = parseFloat(merkit[0]) - parseFloat(merkit[2])
//                     nayta.innerHTML = `${parseFloat(merkit[0])} - ${parseFloat(merkit[2])} = ${vastaus}`;
//                     merkit = []
//                     merkit.push(`${vastaus}`)                        
//                     break;
//                 case "*":
//                     vastaus = parseFloat(merkit[0]) * parseFloat(merkit[2])
//                     nayta.innerHTML = `${parseFloat(merkit[0])} * ${parseFloat(merkit[2])} = ${vastaus}`;
//                     merkit = []
//                     merkit.push(`${vastaus}`)                        
//                     break;
//                 case "/":
//                     vastaus = parseFloat(merkit[0]) / parseFloat(merkit[2])
//                     nayta.innerHTML = `${parseFloat(merkit[0])} / ${parseFloat(merkit[2])} = ${vastaus}`;
//                     merkit = []
//                     merkit.push(`${vastaus}`)                        
//                     break;
//             }
//         }
//     }
// }
