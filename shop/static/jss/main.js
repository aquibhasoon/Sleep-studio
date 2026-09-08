document.addEventListener("DOMContentLoaded", () => {

    // Hero entrance animation
    const heroContent = document.querySelector(".hero-content");
    const heroImage = document.querySelector(".hero-image");

    setTimeout(() => {
        heroContent.classList.add("show");
        heroImage.classList.add("show");
    }, 200);


    // Scroll reveal
    const revealElements = document.querySelectorAll(
        ".section-heading, .mattress-card, .product-category, .feature, .cta, .location"
    );

    const observer = new IntersectionObserver(
        (entries) => {

            entries.forEach((entry) => {

                if (entry.isIntersecting) {
                    entry.target.classList.add("revealed");
                    observer.unobserve(entry.target);
                }

            });

        },
        {
            threshold: 0.15
        }
    );


    revealElements.forEach((element) => {
        element.classList.add("reveal");
        observer.observe(element);
    });

});
document.addEventListener("DOMContentLoaded", function () {

    const filterButtons = document.querySelectorAll(".filter-btn");
    const productCards = document.querySelectorAll(".product-card");

    filterButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const filter = button.dataset.filter;

            filterButtons.forEach(function (btn) {
                btn.classList.remove("active");
            });

            button.classList.add("active");

            productCards.forEach(function (card) {

                const category = card.dataset.category;

                if (filter === "all" || category === filter) {

                    card.style.display = "";
                    
                    requestAnimationFrame(function () {
                        card.style.opacity = "1";
                        card.style.transform = "translateY(0)";
                    });

                } else {

                    card.style.opacity = "0";
                    card.style.transform = "translateY(8px)";

                    setTimeout(function () {
                        card.style.display = "none";
                    }, 300);

                }

            });

        });

    });

});