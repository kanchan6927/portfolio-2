
$(document).ready(function () {
    $(".hamburger").click(function () {
        $(".hamburger").toggleClass("cross");
        $(".homeNav").slideToggle("slow", function () {

        });

    });
});

$(document).ready(function () {
    $('.about-count').each(function () {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 4000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });
});
