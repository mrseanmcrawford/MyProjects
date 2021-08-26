var text = "";                                                  //Defining Variable//
var i;                                                          //Defining Variable//
for (i = 0; i < 10; i++) {                                      //Defining function//
    if (i == 3) { continue; }                                   //Defining function//
    text += "the number is " + i + "<br>";                      //Defining function//
}
document.getElementById("demo").innerHTML = text;           