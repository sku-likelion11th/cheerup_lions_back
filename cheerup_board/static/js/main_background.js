const backgroundImage = document.querySelector('.background-image');
let currentImageIndex = 0;
let fetchedImages = [];

fetch('/get_images/')
.then(response => response.json())
.then(data => {
  fetchedImages = data.images.map(url => `media/${url}`);
  if (fetchedImages.length > 0) {
    changeBackgroundImage(); // Start changing background images
  }
})

function changeBackgroundImage() {
  if (fetchedImages.length === 0) {
    return; // No images to display
  }

  const imageUrl = fetchedImages[currentImageIndex];

  backgroundImage.style.backgroundImage = `url('${imageUrl}')`;
  backgroundImage.style.opacity = 1;

  setTimeout(() => {
    backgroundImage.style.opacity = 0;
  }, 3000);

  currentImageIndex = (currentImageIndex + 1) % fetchedImages.length;
  setTimeout(changeBackgroundImage, 4000);
}