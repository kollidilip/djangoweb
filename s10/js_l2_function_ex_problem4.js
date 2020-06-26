var a = parseInt(prompt("enter the value a"));
var b = parseInt(prompt("enter the value b"));
var c = parseInt(prompt("enter the value c"));

function luckySum(a,b,c) {
  var sum = 0
  if (a == 13)
  {
    return sum;
  }else if (b == 13) {
    sum = a;
    return sum
  } else if (c == 13) {
    sum = a+b;
    return sum;
  }else {
    sum = a+b+c;
    return sum;
  }
  }

console.log("luckySum is : "+luckySum(a,b,c));
alert("luckySum is : "+luckySum(a,b,c));
