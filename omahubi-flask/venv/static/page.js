nayta = (nayttaa) =>{
    switch (nayttaa) {
        case "todo":
            document.getElementById("blogidiv").style.display = "none"
            document.getElementById("calenterdiv").style.display = "none"
            document.getElementById("tododiv").style.display = "flex"
            break;
        case "Write_blog":
            document.getElementById("calenterdiv").style.display = "none"
            document.getElementById("tododiv").style.display = "none"    
            document.getElementById("blogidiv").style.display = "flex"
            break;
        case "calenter":
            document.getElementById("tododiv").style.display = "none"
            document.getElementById("blogidiv").style.display = "none"
            document.getElementById("calenterdiv").style.display = "flex"
            break;
    }
}

const aika = new Date();
const tunti = aika.getHours();
let teksti = "";

if (tunti < 12) {
    teksti = "Good morning"
} else if (tunti >= 12 && tunti < 18) {
    teksti = "Good afternoon"
} else if (tunti >= 18 && tunti < 22) {
    teksti = "Good evening"
}

document.getElementById("teksti").innerHTML = teksti;

let input = document.getElementById("addTask")

let numero = 0;
let tasks = []
let text = ""
input.addEventListener("keypress", takevalues)

function takevalues(e) {
    if (e.code == "Enter") {
        let is = tasks.includes(input.value)
        if (is == true) {
            return;
        } else {
            tasks.push(input.value)
            for (let x in tasks){
                text += tasks[x] + "<br>";
            }
            document.getElementById("task").innerHTML = text;
            text = ""
        }
    }
}

let inputdelete = document.getElementById("DeleteTask")

inputdelete.addEventListener("keypress", DeleteTask)

function DeleteTask(e) {
    if (e.code == "Enter") {
        let index = tasks.indexOf(inputdelete.value)
        if (index > -1) {
            tasks.splice(index, 1)
        }
        for (let x in tasks){
            text += tasks[x] + "<br>";
        }
        document.getElementById("task").innerHTML = text;
        text = ""
    }
}

let t = 0
function mode() {
    t += 1
    if (t == 1) {
        document.getElementById("body").style.backgroundColor = "black";
        document.getElementById("body").style.color = "white";

    } else {
        document.getElementById("body").style.backgroundColor = "white";
        document.getElementById("body").style.color = "black";
        t = 0
    }
}

function daysInMonth(month, year) {
    return new Date(year, month, 0).getDate();
}

function calenter() {
    const kuukaudet = ["tammikuu","helmikuu","maaliskuu","huhtikuu","toukokuu","kesäkuu","heinäkuu","elokuu","syyskuu","lokakuu","marraskuu","joulukuu"];
    const k = new Date();
    const p = new Date();
    const v = new Date();

    let paiva = p.getDate();
    let kk = kuukaudet[k.getMonth()];
    let paiviaKuukaudessa = daysInMonth(v.getFullYear(), p.getDate());

    if (paiviaKuukaudessa == 28) {
        document.getElementById("29").style.display = "none";
        document.getElementById("30").style.display = "none";
        document.getElementById("31").style.display = "none";
    }
    if (paiviaKuukaudessa == 29) {
        document.getElementById("30").style.display = "none";
        document.getElementById("31").style.display = "none";
    }
    if (paiviaKuukaudessa == 30) {
        document.getElementById("31").style.display = "none";
    }
   
    document.getElementById("kuukausi").innerHTML = kk;
    document.getElementById("vuosi").innerHTML = v.getFullYear();

    document.getElementById(`${paiva}`).style.backgroundColor = "#1abc9c";
    document.getElementById(`${paiva}`).style.color = "white";
    document.getElementById(`${paiva}`).style.borderRadius = "5px";
}

calenter()