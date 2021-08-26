var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.font = "30px Arial";
ctx.fillText("Hello World", 10, 50);

function validateForm(0){
    var x = document.forms["myForm"]["fname"].value;
    if (x == "") {
        alert("Name must be filled our");
        return false;
    }
}