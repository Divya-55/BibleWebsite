const optionMenu = document.querySelector(".select-menu");
const selectBtn = document.querySelector(".select-btn");
const sBtn_text = document.querySelector(".sBtn-text");

selectBtn.addEventListener("click", () => {
    optionMenu.classList.toggle("active");
});

optionMenu.addEventListener("click", (event) => {
    if (event.target.classList.contains("option-text")) {
        optionMenu.classList.remove("active");
    }
});
