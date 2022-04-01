// Анимация на сайте
new WOW().init();

// Маски для форм
$("#phoneModal").inputmask({
   "mask": "+1 (ddd) ddd-dddd"
});

$("#phone").inputmask({
   "mask": "+1 (ddd) ddd-dddd"
});

// По умолчанию шапка белая
if ($(window).scrollTop() === 0) {
   $('.header').css("background-color", "transparent");
} else {
   $('.header').css("background-color", "white");
}

// При скроле менять шапку
$(window).scroll(function () {
   if ($(window).scrollTop() === 0) {
      $('.header').css({"background-color": "transparent", "transition": "background 1.0s ease"});
   } else {
      $('.header').css({"background-color": "white", "transition": "background 1.0s ease"});
   }
});


// Инициализация для модальных окон
$(document).ready(function () {
   $('.openModal, .signUp, .signUp2, .signUp3').magnificPopup({
      removalDelay: 500,
      callbacks: {
         beforeOpen: function () {
            this.st.mainClass = this.st.el.attr('data-effect');
         }
      },
      midClick: true
   });

   $(".closeBtn, #doneBtn").click(function () {
      $.magnificPopup.close();
      $('.contactLeftModal').show();
      $(".contactLeftModalSuccess").prop("hidden", !this.checked);
   });
});

