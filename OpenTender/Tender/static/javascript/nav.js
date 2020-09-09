function responsiveNav(){
    var navId= document.getElementById("resnavbar");
    if(navId.className === "navbar"){
        navId.className += " responsive";
    }
    else{
        navId.className = "navbar";
    }
}
