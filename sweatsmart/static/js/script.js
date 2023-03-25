/**
 * Shrinks nav bar, removes padding and adds a black background.
 */

$(window).scroll(function () {
    if ($(document).scrollTop() > 50) {
        $('.nav').addClass('affix');
        console.log("OK");
    } else {
        $('.nav').removeClass('affix');
    }
});

/**
 * This function toggles the "active" class on the navTrigger 
 * element and shows or hides the mainListDiv element when clicked
 */

$('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();

});