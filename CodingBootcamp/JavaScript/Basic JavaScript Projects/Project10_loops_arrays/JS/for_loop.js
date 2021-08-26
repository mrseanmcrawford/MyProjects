var Instruments = ["Guitar", "Drums", "Piano", "Bass", "Violin", "Trumpet", "Flute"];       //Defining variable// 
var Content = "";                                                                           
var Y;
function for_Loop() {                                                                       //Defining "foor_loop" function//
    for (Y = 0; Y < Instruments.length; Y++) {
    Content += Instruments[Y] + "<br>";
    }
    document.getElementById("List_of_Instruments").innerHTML = Content;                     //Get element by id// 
}