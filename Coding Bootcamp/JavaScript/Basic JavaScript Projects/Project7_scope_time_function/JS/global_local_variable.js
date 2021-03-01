//Global Variable//
var x = 20; 
function Add_numbers_1() {
    document.write(20 + x + "<br>");
}
function Add_numbers_2() {
    document.write(x + 100 + "<br>");
}
Add_numbers_1();
Add_numbers_2();


//Local  Variable// 
function Add_numbers_12() {
    var x = 10;
    document.write(20 + x + "<br>");
}
function Add_numbers_22() {
   console.log(x + 100);
}
Add_numbers_12();
Add_numbers_22();