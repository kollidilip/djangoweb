var weekday = prompt("is it a weekday : true or false")
var vacation = prompt("is it a vacation : true or false")

if (weekday == "true") {
  weekday = true
} else{
  weekday = false
}

if (vacation == "true") {
  weekday = true
} else{
  vacation = false
}

issleeping =sleepIn(weekday,vacation)
console.log("issleeping: "+issleeping);

function sleepIn(weekday,vacation) {
  console.log("weekday : "+weekday);
  console.log("vacation : "+vacation);
  if(! weekday || vacation){
    var sleep = true
  } else {
    var sleep = false
  }
  return sleep
}
