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

document.addEventListener("DOMContentLoaded", () => {
    const rajaanappi = document.querySelectorAll("#ul li");
    const reseptidiv = document.querySelectorAll(".recipe-card");

    rajaanappi.forEach(button => {
        button.addEventListener("click", () => {
            const kategoria = button.textContent.trim().toLowerCase();

            reseptidiv.forEach(card => {
                const ruokaKatekoria = card.dataset.category.toLowerCase();
                

                if (kategoria === "all" || ruokaKatekoria === kategoria) {
                    card.style.display = "block"
                    ;
                } else {
                    card.style.display = "none";
                }

            });
        });
    });
});