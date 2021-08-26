var text = "";
var i;
for (i = 0; i < 10; i++) {
    if (i == 3) { continue; }
    text += "the number is " + i + "<br>";
}
document.getElementById("demo").innerHTML = text;