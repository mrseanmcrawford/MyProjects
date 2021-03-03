function countdown() {                                              //defining function//
    var seconds = document.getElementById("seconds").value;         //defining variable//

    function tick() {                                               //creating function within variable 
        seconds = seconds - 1;                                      //defining function//
        timer.innerHTML = seconds;                                  //defining function//
        setTimeout(tick, 1000);                                     //defining function//
    if(seconds == -1) {                                             //defining 'IF' function//
        alert("Time has ended!");                                        //defining 'alert function//
    }
        }
    tick();                                                        //creating tick function//
}