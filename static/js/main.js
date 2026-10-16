

document.addEventListener("DOMContentLoaded", function () {



    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    if (menuToggle && navLinks) {

        menuToggle.addEventListener("click", function () {

            const isOpen = navLinks.classList.toggle("open");

            menuToggle.setAttribute(
                "aria-expanded",
                String(isOpen)
            );

            const icon = menuToggle.querySelector("i");

            if (icon) {
                icon.className = isOpen
                    ? "bi bi-x-lg"
                    : "bi bi-list";
            }

        });

        navLinks.querySelectorAll("a").forEach(function (link) {

            link.addEventListener("click", function () {

                navLinks.classList.remove("open");

                menuToggle.setAttribute(
                    "aria-expanded",
                    "false"
                );

                const icon = menuToggle.querySelector("i");

                if (icon) {
                    icon.className = "bi bi-list";
                }

            });

        });

        document.addEventListener("keydown", function (event) {

            if (event.key === "Escape") {

                navLinks.classList.remove("open");

                menuToggle.setAttribute(
                    "aria-expanded",
                    "false"
                );

                const icon = menuToggle.querySelector("i");

                if (icon) {
                    icon.className = "bi bi-list";
                }

            }

        });

    }


    // ======================================
    // 2. SHOW / HIDE PASSWORD
    // ======================================

    document.querySelectorAll(".password-toggle").forEach(
        function (button) {

            button.addEventListener("click", function () {

                const wrapper = button.closest(".input-wrap");

                if (!wrapper) {
                    return;
                }

                const passwordInput = wrapper.querySelector("input");

                if (!passwordInput) {
                    return;
                }

                const isPassword = passwordInput.type === "password";

                passwordInput.type = isPassword
                    ? "text"
                    : "password";

                const icon = button.querySelector("i");

                if (icon) {
                    icon.className = isPassword
                        ? "bi bi-eye-slash"
                        : "bi bi-eye";
                }

                button.setAttribute(
                    "aria-label",
                    isPassword
                        ? "Parolni yashirish"
                        : "Parolni ko‘rsatish"
                );

            });

        }
    );


    // ======================================
    // 3. SCROLL REVEAL ANIMATIONS
    // ======================================

    const revealElements = document.querySelectorAll(".reveal");

    const reduceMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    if (
        revealElements.length &&
        !reduceMotion &&
        "IntersectionObserver" in window
    ) {

        document.documentElement.classList.add("js-enabled");

        const revealObserver = new IntersectionObserver(
            function (entries, observer) {

                entries.forEach(function (entry) {

                    if (entry.isIntersecting) {

                        entry.target.classList.add("visible");

                        observer.unobserve(entry.target);

                    }

                });

            },
            {
                threshold: 0.08,
                rootMargin: "0px 0px -25px 0px"
            }
        );

        revealElements.forEach(function (element) {

            revealObserver.observe(element);

        });

    }


    // ======================================
    // 4. NAVBAR SCROLL EFFECT
    // ======================================

    const navbar = document.querySelector(".navbar");

    function updateNavbar() {

        if (!navbar) {
            return;
        }

        if (window.scrollY > 20) {

            navbar.style.boxShadow =
                "0 12px 35px rgba(0,0,0,.22)";

        } else {

            navbar.style.boxShadow = "none";

        }

    }

    updateNavbar();

    window.addEventListener(
        "scroll",
        updateNavbar,
        { passive: true }
    );


    // ======================================
    // 5. BUTTON LOADING STATE
    // ======================================

    document.querySelectorAll(
        "form[action*='subscribe']"
    ).forEach(function (form) {

        form.addEventListener("submit", function () {

            const button = form.querySelector(
                "button[type='submit']"
            );

            if (!button) {
                return;
            }

            button.disabled = true;

            button.innerHTML =
                '<i class="bi bi-hourglass-split"></i> Yuborilmoqda...';

        });

    });



    console.log(
        "%cFITCLUB",
        "color:#b7f34b;font-size:22px;font-weight:bold;"
    );

    console.log("FitClub frontend initialized.");

});
