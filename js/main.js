/* ========================================
   Main JavaScript — Navigation, Scroll, Animations
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {
    initI18n();
    initNavigation();
    initScrollAnimations();
    initSmoothScroll();
    initVideoEmbeds();
});

/* --- Navigation --- */
function initNavigation() {
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('.nav-links a');

    // Scroll effect on navbar
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 50);
        updateActiveNavLink();
    });

    // Mobile menu toggle
    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('open');
    });

    // Close mobile menu on link click
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            navMenu.classList.remove('open');
        });
    });

    // Close mobile menu on outside click
    document.addEventListener('click', (e) => {
        if (!navbar.contains(e.target) && navMenu.classList.contains('open')) {
            navToggle.classList.remove('active');
            navMenu.classList.remove('open');
        }
    });
}

/* --- Active Nav Link on Scroll --- */
function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links a');
    const scrollPos = window.scrollY + 100;

    sections.forEach(section => {
        const top = section.offsetTop;
        const height = section.offsetHeight;
        const id = section.getAttribute('id');

        if (scrollPos >= top && scrollPos < top + height) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${id}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}

/* --- Scroll Fade-In Animations --- */
function initScrollAnimations() {
    const fadeElements = document.querySelectorAll('.fade-in');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Stagger animation for siblings
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 100);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    fadeElements.forEach(el => observer.observe(el));
}

/* --- Smooth Scroll --- */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const target = document.querySelector(targetId);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

/* --- Convert Video Thumbnails to YouTube Embeds --- */
function initVideoEmbeds() {
    document.querySelectorAll('.video-thumb').forEach(thumb => {
        const href = thumb.getAttribute('href');
        if (!href) return;

        const match = href.match(/[?&]v=([^&]+)/);
        if (!match) return;

        const videoId = match[1];
        const label = thumb.querySelector('.video-label');
        const labelText = label ? label.textContent : '';

        // Create embed wrapper
        const wrapper = document.createElement('div');
        wrapper.className = 'video-embed';

        const iframe = document.createElement('iframe');
        iframe.src = `https://www.youtube.com/embed/${videoId}`;
        iframe.setAttribute('allowfullscreen', '');
        iframe.setAttribute('loading', 'lazy');
        iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
        iframe.setAttribute('frameborder', '0');
        iframe.title = labelText || 'YouTube video';

        wrapper.appendChild(iframe);

        if (labelText) {
            const labelEl = document.createElement('span');
            labelEl.className = 'video-label';
            labelEl.textContent = labelText;
            if (label && label.hasAttribute('data-i18n')) {
                labelEl.setAttribute('data-i18n', label.getAttribute('data-i18n'));
            }
            wrapper.appendChild(labelEl);
        }

        thumb.replaceWith(wrapper);
    });
}