function my_Dictionary() {                                  // defining function
    var City = {                                            // naming variable 
       Name: "Seattle",                                     // Descfribing variable 
       Region: "PNW",
       State: "Washington",
       Country: "USA"
    };
    delete City.Name;                                       // Deleting Name 
    document.getElementById("Dictionary").innerHTML = City.State
};