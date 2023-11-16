document.addEventListener('DOMContentLoaded', function() {
    var img_dir = "frontpage_images/";
    var images = [
        img_dir + 'plant_1.jfif',
        img_dir + 'plant_2.jfif',
        img_dir + 'plant_3.jfif',
        img_dir + 'plant_4.jfif',
        img_dir + 'plant_5.jfif',


    ];
    var imageSets = document.querySelectorAll('.image-set');

    // Set initial images in both sets
    images.forEach(function(image) {
        var placeholder = document.createElement('div');
        placeholder.className = 'image-placeholder';
        placeholder.style.backgroundImage = 'url(' + image + ')';
        imageSets[0].appendChild(placeholder.cloneNode(true));
        imageSets[1].appendChild(placeholder);
    });

    var galleryContainer = document.querySelector('.gallery-container');
    var offset = 0;

    function slideImages() {
        offset -= 1; // Adjust this value for the sliding speed
        galleryContainer.style.transform = 'translateX(' + offset + '%)';

        // Check if the first set of images is out of view, then reset the offset
        if (-offset >= 10) {
            offset = 0;
        }
    }

    setInterval(slideImages, 100); // Adjust the interval for the sliding speed
});
