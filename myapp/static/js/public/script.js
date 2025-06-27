


// testmonials btn start ===========================
// var TrandingSlider = new Swiper('.tranding-slider', {
//     effect: 'coverflow',
//     grabCursor: true,
//     centeredSlides: true,
//     loop: true,
//     slidesPerView: 'auto',
//     coverflowEffect: {
//       rotate: 0,
//       stretch: 0,
//       depth: 100,
//       modifier: 2.5,
//     },
//     pagination: {
//       el: '.swiper-pagination',
//       clickable: true,
//     },
//     navigation: {
//       nextEl: '.swiper-button-next',
//       prevEl: '.swiper-button-prev',
//     },
//     on: {
//       slideChange: function () {
//           document.querySelectorAll('.tranding-slide').forEach(function (slide) {
//               slide.classList.remove('tranding-slide-active');
//           });

//           var activeSlide = this.slides[this.activeIndex];
//           activeSlide.classList.add('tranding-slide-active');

//           // Remove 'active-image' class from all images
//           document.querySelectorAll('.responsive-div img').forEach(function (img) {
//               img.classList.remove('active-image');
//           });

//           // Add 'active-image' class to the active image
//           var activeImage = activeSlide.querySelector('.responsive-div img');
//           activeImage.classList.add('active-image');
//       },
//   },
//   });
  
// testmonials btn start ===========================
var TrandingSlider = new Swiper('.tranding-slider', {
  effect: 'coverflow',
  grabCursor: true,
  centeredSlides: true,
  loop: true,
  slidesPerView: 'auto',
  coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 100,
      modifier: 2.5,
  },
  pagination: {
      el: '.swiper-pagination',
      clickable: true,
  },
  navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
  },
  autoplay: {
      delay: 5000, // Autoplay delay in milliseconds (adjust as needed)
      disableOnInteraction: false, // Allow manual navigation while autoplay
  },
  on: {
      slideChange: function () {
          document.querySelectorAll('.tranding-slide').forEach(function (slide) {
              slide.classList.remove('tranding-slide-active');
          });

          var activeSlide = this.slides[this.activeIndex];
          activeSlide.classList.add('tranding-slide-active');

          // Remove 'active-image' class from all images
          document.querySelectorAll('.responsive-div img').forEach(function (img) {
              img.classList.remove('active-image');
          });

          // Add 'active-image' class to the active image
          var activeImage = activeSlide.querySelector('.responsive-div img');
          activeImage.classList.add('active-image');
      },
  },
});

// testmonials btn end ===========================  


// testmonials btn end ===========================

let calcScrollValue = () => {
  let scrollProgress = document.querySelector('#progress');
  let pos = document.documentElement.scrollTop;
  let calcHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  let scrollValue = Math.round((pos * 100 )/ calcHeight);

  // console.log(scrollValue);
  if(pos>100){
    scrollProgress.style.display = "grid";
}else{
    scrollProgress.style.display = "none";
}

scrollProgress.addEventListener('click', () => {
  document.documentElement.scrollTop = 0;
});

scrollProgress.style.background = `conic-gradient(#03cc65 ${scrollValue}%, #d7d7d7 ${scrollValue}%)`;

let scrollProgress_whatsApp = document.querySelector('#progress-whatsApp');
let pos_whatsApp = document.documentElement.scrollTop;
let calcHeight_whatsApp = document.documentElement.scrollHeight - document.documentElement.clientHeight;
let scrollValue_whatsApp = Math.round((pos * 100 )/ calcHeight);

// console.log(scrollValue);
if(pos>100){
  scrollProgress_whatsApp.style.display = "grid";
}else{
  scrollProgress_whatsApp.style.display = "none";
}

scrollProgress_whatsApp.addEventListener('click', () => {
document.documentElement.scrollTop = 0;
});

scrollProgress_whatsApp.style.background = `conic-gradient(#03cc65 ${scrollValue}%, #d7d7d7 ${scrollValue}%)`;

};
  
window.onscroll = calcScrollValue;
window.onload = calcScrollValue;

let calcScrollValue2 = () => {
  let scrollProgress = document.querySelector('#progress-whatsApp');
  let pos = document.documentElement.scrollTop;
  let calcHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  let scrollValue = Math.round((pos * 100 )/ calcHeight);

  // console.log(scrollValue);
  if(pos>100){
    scrollProgress.style.display = "grid";
}else{
    scrollProgress.style.display = "none";
}

scrollProgress.addEventListener('click', () => {
  document.documentElement.scrollTop = 0;
});

scrollProgress.style.background = `conic-gradient(#03cc65 ${scrollValue}%, #d7d7d7 ${scrollValue}%)`;

};

// window.onscroll = calcScrollValue2;
// window.onload = calcScrollValue2;