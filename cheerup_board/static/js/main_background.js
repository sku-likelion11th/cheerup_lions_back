const images = [
    '/static/img/start2.jpg',
    '/static/img/start.jpg',
  ];
  
const backgroundImage = document.querySelector('.background-image');
let currentImageIndex = 0;

fetch('/get_images/')
.then(response => response.json())
.then(data => {
  const fetchedImage = data.images.map(url => `media/${url}`);
  images.push(...fetchedImage);
})

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
