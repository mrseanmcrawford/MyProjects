//Else-If Statement && Time_function()//
function Time_function() {                                      //Naming and defining function
    var Time = new Date().getHours();                           //Naming Variables
    var Reply;
    if (Time < 12 == Time > 0) {                                //If Statment
        Reply = "It is morning time";
    }
    else if (Time >= 12 == Time < 18) {                         //Else-If Statement
        Reply = "It is afternoon";
    }
    else {
        Reply = "It is evening time";                           //Else Statement 
    }
    console.log()
    document.getElementById("Time_of_day").innerHTML = Reply;
}

//Global and local Variables//
//Global Variable
var x = 20;                                                     //Defining Variable 
function Add_numbers_1() {                                      
    document.write(20 + x + "<br>");                            //Function instructions 
}
function Add_numbers_2() {                                      //Defining Variable 
    document.write(x + 100 + "<br>");                          //Function instructions
}
Add_numbers_1();
Add_numbers_2();


//Local  Variable// 
function Add_numbers_12() {                                  //Assigning/Defining function 
    document.write(20 + x + "<br>");                         //Function instructions
}
function Add_numbers_22() {
   console.log(x + 100);
}
Add_numbers_12();
Add_numbers_22();
