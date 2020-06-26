var speed = parseInt(prompt("Please enter the speed"))
var isbday = false
    if (speed < 0) {
      alert("please enter a valid speed")
    } else {
      var isbday = prompt("Is today your birthday","yes or no")
      if (isbday === "yes") {
        isbday = true
      } else if (isbday === "no") {
        isbday = true
      } else {
        alert("you have to enter either yes or no")
      }
    }

function caught_speeding(speed,isbday) {
  var ticket = 0;
      if (isbday) {
        if (speed >= 0 && speed <= 60) {
          ticket = 0
        } else if (speed > 60 && speed <= 80) {
          ticket = 1;
        }else if(speed > 80) {
          ticket = 2;
        }
      } else {
        if (speed > 0 && speed <= 65) {
          ticket = 0
        } else if (speed > 65 && speed < 85) {
          ticket = 1;
        }else if(speed > 80){
          ticket = 2;
        }
      }
      return ticket;
    }

alert("The speeding offence ticket charged is : "+caught_speeding(speed,isbday))
console.log("The speeding offence ticket charged is : "+caught_speeding(speed,isbday));
