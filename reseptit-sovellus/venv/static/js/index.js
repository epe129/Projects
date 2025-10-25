let t = 0

function myadd() {
    t += 1
    if (t == 1) {
        document.getElementById("ADDdiv").style.display = "flex";
    } else {
        document.getElementById("ADDdiv").style.display = "none";
        t = 0                
    }
}