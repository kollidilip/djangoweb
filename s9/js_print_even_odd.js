var n = prompt("enter a value of n to get the even numbers from 0 to n");
var i = 0;
while (i <= n) {
    // check for even numbers
    if (i === 0) {
      console.log(i +" is neither even nor odd number");
    }else if (i % 2 == 0) {
      console.log(i +" is even number");
    }else {
      console.log(i +" is odd number");      
    }
    i++;
}
