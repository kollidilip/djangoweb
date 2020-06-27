
var roster = [];

doyouWant();
function roSter(x) {
  var i;
  if (x === "add") {
    var a = prompt("enter a name to add");
    i = roster.push(a);
  }else if (x === "remove") {
    i = roster.pop();
  }else if (x === "display") {
    alert("the roster is as this : "+ roster);
  }else if (x === "quit") {
    thankYou();
  }
reload();
}

function doyouWant(){
  var w = prompt(" Do you want to enter the roster app y/n")
  if(w == 'y'){
    reload();
  }else {
    alert("Thank you!")
  }
}

function reload() {
  var x = prompt("Select the action 1. add, 2. remove, 3. display, 4.quit")
  roSter(x);
}
