function validate() {
    if (document.getElementById(botCount).value == '' || document.getElementById(playerCount).value) {
        alert("test")
        let btnNext = document.getElementById(btnNext);
        btnNext.disabled = true;
    }
}