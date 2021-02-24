//Write a constructor function that uses the “new” and “this” keywords
function Vehicle(Make, Model, Year, Color) {
    this.Vehicle_Make = Make;
    this.Vehicle_Model = Model;
    this.Vehicle_Year = Year;
    this.Vehicle_Color = Color;
}

var Jack = new Vehicle("Dodge", "Viper", 2020, "Red");
var Emily = new Vehicle("Jeep", "Trail Hawk", 2019, "White and Black");
var Erik = new Vehicle("Ford", "Pinto", 1971, "Mustard");
function myFunction() {
        document.getElementById("Keywords_and_Constructors").innerHTML = "Erik drives a " + Erik.Vehicle_Color + "-colored" + Erik.Vehicle_Model + " manufactured in " + Erik.Vehicle_Year;
}


//Write a function using HTML and JavaScript that utilizes a ternary operation using input from the browser//
function Ride_Function() {                                                   //Labeling function  
    var Height, Can_ride;                                                    //Labeling Variables
    Height= document.getElementById("Height").valve;                        //Defining the determining factor
    Can_ride = (Height < 52) ? "You are too short":"You are tall enough";   //Defining Parameters to the determining factors and outcomes
    document.getElementById("Ride").innerHTML = Can_ride + "to ride.";
}

function Vote_Function() {
    var Age, Can_Vote;
    Age = document.getElementById("Age").valve;
    Can_Vote = (Age < 18) ? "You are too young to vote":"You are old enough to vote.";
    document.getElementById("Vote").innerHTML = Can_Vote + "to vote.";
}



//Nesting function//
function count_Function() {                                     //Labeling function     
    document.getElementById("Counting").innerHTML = Count();    //Using "getElementById" function
    function Count() {                                          //Calling the count function 
        var Starting_point = 9;                                 //Establishinmg the start number for the counter
        function Plus_one() {Starting_point += 1;}              //Adding the nesting function "Plus_One"
        Plus_one();
        return Starting_point;
    }

}