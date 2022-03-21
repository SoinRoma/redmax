$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 15,
        responsive: {
            0: {
                items: 1
            },
            640: {
                items: 2
            },
            795: {
                items: 3
            },
            1000: {
                items: 3
            }
        }
    });
});
