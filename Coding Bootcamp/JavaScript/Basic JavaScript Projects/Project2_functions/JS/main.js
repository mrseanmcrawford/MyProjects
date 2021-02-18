function My_First_Function() {                                      //defining a function and naming it
    var str = "This text is green!";                                // defining a variable and giving it a name 
    var result = str.fontcolor("green");                            //using fomt color methon on string variable
    document.getElementById("Green_Text").innerHTML = result;       // putting the value of the result into the HTML element with "Green_Text" id
}
