var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

//Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {                                                //Defining Slideshow function//
    var i;                                                              //Defining Variable//
    var slides = document.getElementsByClassName("mySlides");           //Defining Variable//
    var dots = document.getElementsByClassName("dot");                 //Defining  Variable//
    if (n > slides.length) {slideIndex = 1}                            // "IF" Property//
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {                              //"For" Property//
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
}