var fname = prompt("Please enter your first name");
var lname = prompt("Please enter your last name");
var age = prompt("Please enter your age name");
var height = prompt("Please enter your height in cms");
var pname = prompt("Please enter your pet name");
alert("Thanks for your information")
// check if the first name and second name starts with same character
if (fname[0] === lname[0]) {
  if (age > 20 && age < 30) {
    if (height >= 170) {
      if (pname[pname.length-1] === 'y') {
        console.log("welcome agent! pleased to interact with you");
      }
    }
  }
}else {
  console.log("sorry nothing to view here");
}
