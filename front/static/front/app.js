const navSlide = () => {
    const bruger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    bruger.addEventListener('click', () => {
        // nav animation
        nav.classList.toggle('nav-active');

        // nav link animations
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ""
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
            }
    
        });
        // close nav animation
        bruger.classList.toggle('toggle');
    });
    
}

navSlide();