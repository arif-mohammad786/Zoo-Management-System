if(window.matchMedia("(max-width:600px)").matches){
    var abt=document.getElementById("aboutzooid");
    abt.classList.remove("rounded-pill")
    /*var md=document.getElementById("midid");
    md.classList.add("offset-1")*/
}else{
    var abt=document.getElementById("aboutzooid");
    abt.classList.add("rounded-pill")
}