    function constant_function() {
        const Musical_Instrument = {tyoe: "guitar", brand:"Fender", color:"black"};
        Musical_Instrument.color = "blue";
        Musical_Instrument.price = "$900";
        document.getElementById("Constant").innerHTML = "The cost of the " +
            Musical_Instrument.tyoe + " was " + Musical_Instrument.price;
    }