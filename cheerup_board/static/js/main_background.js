const images = [
    '/static/img/IMG_1.jpg',
    '/static/img/IMG_2.jpg',
    '/static/img/IMG_3.jpg',
    '/static/img/IMG_4.jpg',
    '/static/img/IMG_5.jpg',
    '/static/img/IMG_6.jpg'
  ];
  
  const backgroundImage = document.querySelector('.background-image');
  let currentImageIndex = 0;
  
  function changeBackgroundImage() {
    backgroundImage.style.backgroundImage = `url('${images[currentImageIndex]}')`;
    backgroundImage.style.opacity = 1;
    
    setTimeout(() => {
      backgroundImage.style.opacity = 0;
    }, 3000);
  
    currentImageIndex = (currentImageIndex + 1) % images.length;
    setTimeout(changeBackgroundImage, 4000);
  }
  
  changeBackgroundImage();
  