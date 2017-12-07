var mySwiper = new Swiper ('.swiper-container', {
    // Settings
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 'auto',
    coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: false,
    },
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
});