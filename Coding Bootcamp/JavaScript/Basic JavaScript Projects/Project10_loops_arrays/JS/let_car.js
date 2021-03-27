let car = {                                                                                  //Defining Variable//
    make: "Jeep ",                                                                           //Defining Function//
    model: "Grand Wagoneer ",                                                                //Defining Function//
    year: "2022 ",                                                                           //Defining Function//
    color: "black ",                                                                         //Defining Function//
    description : function() {                                                               //Defining Function//      
        return "The car is a " + this.year + this.color + this.make + this.model;            //Defining Function//
        }
};
document.getElementById("Car_Object").innerHTML = car.description();                        