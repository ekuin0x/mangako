$(window).ready(()=>{
    AOS.init();
})

$("nav a").click(function(){
    let sub = $(this).text()
    if($(`#${sub}`).css("height") == '350px' ){
        $(`#${sub}`).css("height" ,"0")
    }else{
        $(`#${sub}`).css("height" ,"350px")
    }
})

const scroller = (elem)=>{
    $("html, body").animate({scrollTop : $(elem).offset().top }, 700)
}
const openNav = function(){
    $("#mobile-nav").animate({"width" : "100vw"}, 300)
}
const closeNav = function(){
    $("#mobile-nav").animate({"width" : "0"},300)
}


const search = function(elem){
    console.log("HELLO FROM SEARCH")
    let q = $(elem).val()
    window.location.href = "/search/" + q
}

