function cat_pics() {                               //Defining function//   
    var Cat_Picture = [];                          //Defining variable//
    Cat_Picture[0] = "sleeping";                  //Defining array//
    Cat_Picture[1] = "playing";
    Cat_Picture[2] = "eating";
    Cat_Picture[3] = "purring";
    document.getElementById("Cat").innerHTML = "In this picture, the cat is " +     //GetElementByID//
        Cat_Picture[2] + ".";
}