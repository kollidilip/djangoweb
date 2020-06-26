
var sbrick = parseInt(prompt("Enter the number of small bricks(1 inch length)"));
var bbrick = parseInt(prompt("Enter the lenght of big brick(5 inch length)"));
var goalln = parseInt(prompt("Enter the lenght of goal post"));

function makeBrick(sbrick,bbrick,goalln) {
  var bl =5; // bigbrick lenght
  var sl =1; // small brick length
  if ((sbrick*sl + bbrick*5) >= goalln) {
    return true;
  } else {
    return false;
  }
}

alert("can the goal post be built : "+ makeBrick(sbrick,bbrick,goalln))
