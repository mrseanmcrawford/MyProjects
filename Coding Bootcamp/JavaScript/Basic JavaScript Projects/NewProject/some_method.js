var ages = [2, 10, 18, 20, 13, 15, 30];
//Using the arrow function to pass in a parameter of age
checkAge = {age} => age >= 18;

function myFunction() {
    //Use the .some() to iterate through the array of ages and display the result.
    document.getElementById('displayAge').innerHTML = ages.some(checkAge);
}