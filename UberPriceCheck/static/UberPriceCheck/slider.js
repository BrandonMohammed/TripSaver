var slider = document.getElementById("myDistance");
var output = document.getElementById("demo");
output.innerHTML = slider.value;
    
slider.oninput = function() {
    output.innerHTML = this.value;
}