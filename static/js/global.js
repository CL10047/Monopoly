document.addEventListener("DOMContentLoaded", function() {
    rollDice();
});

function rollDice() {
    let diceRoll = Math.floor(Math.random() * 6) + 1;
    alert('You rolled a ' + diceRoll);
}