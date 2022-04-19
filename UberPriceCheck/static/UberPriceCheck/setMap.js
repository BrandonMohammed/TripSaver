function setMap(clicked_id){
    var destination = document.getElementById("currentAddress").innerHTML;

    var frame = document.getElementById("mapFrame")
    frame.src = ("https://www.google.com/maps/embed/v1/directions?key=AIzaSyDeH51N2UWKt1xunMRHRY5JZiie1S5ZdeE&origin="
                                + clicked_id.toString() + "&destination=" + destination + "&avoid=tolls|highways")
}