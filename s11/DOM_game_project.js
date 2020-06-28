// get all squares
var square = document.querySelectorAll("td");

// set the event listner for the reset button
var reset = document.querySelector("button")
reset.addEventListener("click",resetall)

// reset the squares
function resetall() {
for (var i = 0; i < square.length; i++) {
  square[i].textContent = " ";
}
}

// addEventListener to squares
for (var i = 0; i < square.length; i++) {
  square[i].addEventListener("click",fillSquare)
}

// Assign the square with click
function fillSquare() {
  if (this.textContent === " ") {
    this.textContent = "X";
  }else if (this.textContent === "X") {
    this.textContent = "O";
  }else{
    this.textContent = " ";
  }
}
