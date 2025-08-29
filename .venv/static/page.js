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