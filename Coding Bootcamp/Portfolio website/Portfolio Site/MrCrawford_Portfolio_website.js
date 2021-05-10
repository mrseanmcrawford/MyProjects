// These functions open and close the contact form
function openForm() {
    document.getElementById("myForm").style.display = "block";
}
function closeForm() {
    document.getElementById("myForm").style.display= "none";
}


// This function displays the first image in the slideshow when the page loads
var slideIndex = 1;
showSlides(slideIndex);

//This function changes the slide when the left or the right arrows are clicked
function plusSlides(n) {
    showSlides(slideIndex += n);
}

//This function changes the slide when the dots are clicked
function currentSlide(n) {
showSlides(slideIndex = n);
}

function showSlides(n) {
    var slides = document.getElementsByClassName("mySlides"); // This takes all elements with the class name "my slides" and stores them in the variable array "slides"
    var dots = documemt.getElementsByClassName("dot"); // This takes all elements with the class name "dot" and stores them in the variable array "dots"
    if (n > slides.length)  {slideIndex = 1}; // if n (the number passed onto the function) is greater than the length of the array "slides", the slideIndex is sert to 1
    if (n < 1) {slideIndex = slide.length}; // if n (the number passed into the function) ois less than 1, the slideIndex is set to the length of the array "slides"
    for (i = 0; i < slides.length; i++) {
            slides[i].style.display = none; // This for loop takes each item in the array "dots" and removes "active" which removes the active stling
        }

    for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", ""); // This 
            // for loop takes each item in the array "dots" and removes "active" which removes the active styling
        }
    slides[slideIndex - 1].style.display = "block"; // This displays the image in the slideshow
    dots[slideIndex - 1].className += " active"; // This adds the active styling to the dot associated with
}