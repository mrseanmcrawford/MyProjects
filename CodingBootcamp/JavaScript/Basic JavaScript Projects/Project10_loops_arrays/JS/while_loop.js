var text = "";                                              //Defining variable//
var i = 0;                                                  
while (i < 10) {                                           //Defining "while" function//
  text += "<br>The number is " + i;
  i++;                  
}
document.getElementById("demo").innerHTML = text;          //Get element by id//