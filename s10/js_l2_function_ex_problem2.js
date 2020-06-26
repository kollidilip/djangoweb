var aSmile = prompt("Is monkey A smiling: if yes enter '1' else enter '0'");
var bSmile = prompt("Is monkey B smiling: if yes enter '1' else enter '0'");

if (aSmile === "1"){
  aSmile = true;
}else {
  aSmile = false;
}

if (bSmile === "1"){
  bSmile = true;
}else {
  bSmile = false;
}
var montrouble = false;
function monkeyTrouble(aSmile,bSmile) {
  if (aSmile === bSmile) {
      montrouble = true;
  }else {
    montrouble = false;
  }
  return montrouble;
}

console.log(monkeyTrouble(aSmile,bSmile));
alert("Monkey trouble is :"+ monkeyTrouble(aSmile,bSmile))
