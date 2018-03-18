/*---------------------
INICIAMOS WOW
----------------------*/

new WOW().init();

/*-----------------------------------
Iniciamos smoothScroll (Scroll Suave)
------------------------------------*/

smoothScroll.init({
    selector: '[data-scroll]', // Selector for links (must be a class, ID, data attribute, or element tag)
    selectorHeader: null, // Selector for fixed headers (must be a valid CSS selector) [optional]
    speed: 1000, // Integer. How fast to complete the scroll in milliseconds
    easing: 'easeInOutCubic', // Easing pattern to use
    offset: 60, // Integer. How far to offset the scrolling anchor location in pixels
    callback: function ( anchor, toggle ) {} // Function to run after scrolling
});

/*-----------------------
OCULTAR BOTON IR ARRIBA
------------------------*/

 $(function () {
    $(window).scroll(function () {
        var scrolltop = $(this).scrollTop();
            $(".ir-arriba").hide;
            if (scrolltop >= 50) {
                $(".ir-arriba").fadeIn(1000);
            } else {
                $(".ir-arriba").fadeOut();
            }
        });
    });

/*---------------------------------
   CABECERA ANIMADA
 ----------------------------------*/
$(window).scroll(function () {

    var nav = $('.encabezado');
    var scroll = $(window).scrollTop();

    if (scroll >= 100) {
        nav.addClass("fondo-menu");
    } else {
        nav.removeClass("fondo-menu");
    }
});
