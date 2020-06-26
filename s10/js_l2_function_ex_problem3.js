alert("i am running")
var n = prompt("enter an interger > 0");
var str = prompt("enter the string to be multiplied")
if (n>0) {
  var strout = stringTimes(str,n)
  alert("the multiplied string is :"+strout)
}else {
  alert("please enter an +ve integer value")
}


  function stringTimes(str,n) {
    var i = 0;
    str1 ="";
  while (i <= n) {
    str1 = str1+str;
    i++
    }
  return str1
  }
