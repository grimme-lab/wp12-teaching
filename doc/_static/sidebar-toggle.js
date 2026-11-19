document.addEventListener("DOMContentLoaded", () => {
    const toggles = Array.from(document.querySelectorAll(".primary-toggle"));
    const themeToggle = toggles[0];

    // The theme binds only the first button, which may be in a hidden header.
    // Forward the remaining buttons to it to retain the theme's responsive behavior.
    toggles.slice(1).forEach((toggle) => {
        toggle.addEventListener("click", (event) => {
            event.preventDefault();
            event.stopImmediatePropagation();
            themeToggle.click();

            const dialog = document.getElementById("pst-primary-sidebar-modal");
            if (dialog && dialog.open) {
                dialog.addEventListener("close", () => toggle.focus(), { once: true });
            } else {
                toggle.focus();
            }
        }, true);
    });
});
