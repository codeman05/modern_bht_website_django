var mySwiper = new Swiper ('.swiper-container', {
    // Settings
    effect: 'flip',
    grabCursor: true,
    loop: true,

    // Pagination settings
    pagination: {
      el: '.swiper-pagination',
    },

    // Navigation settings
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    // And if we need scrollbar
    //scrollbar{
    //  el: '.swiper-scrollbar',
    //},
});
