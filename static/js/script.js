document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.fade-in');
  
    function debounce(func, wait = 20, immediate = true) {
      let timeout;
      return function () {
        const context = this,
          args = arguments;
        const later = function () {
          timeout = null;
          if (!immediate) func.apply(context, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
      };
    }
  
    function checkSlide() {
      images.forEach((image) => {
        const slideInAt =
          window.scrollY + window.innerHeight - image.height / 2;
        const imageBottom = image.offsetTop + image.height;
        const isHalfShown = slideInAt > image.offsetTop;
        const isNotScrolledPast = window.scrollY < imageBottom;
  
        if (isHalfShown && isNotScrolledPast) {
          image.style.opacity = 1;
        }
      });
    }
  
    window.addEventListener('scroll', debounce(checkSlide));
  });
  