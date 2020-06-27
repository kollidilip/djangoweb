// json employee object

var empObj = {
  "name" : prompt("Hi there, Please enter your name"),
  "age" : parseInt(prompt("Hi there, enter your age")),
  "job" : "programmer",
  "nameLength"  : function(){
    var lg = this.name.length
    alert("namelength is : "+lg)
  },
  "lastName" : function(){
      // last nameLength
      var lname = this.name.split(' ');
      alert("Last name is : "+lname[1])
    }
}
empObj.nameLength()
alert("name is : "+empObj["name"])
alert("age is : "+empObj["age"])
alert("Job is : "+empObj["job"])
empObj.lastName()
