var text = "";                                                    //Defining Variable//
var i;                                                           //Defining Variable//
for (i = 0; i < 10; i++) {                                       //Defining Function//
    if (i === 3) { break; }                                      //Defining Function//
    text += "The number is " + i + "<br>";                       //Defining Function//
}
document.getElementById("demo").innerHTML = text;