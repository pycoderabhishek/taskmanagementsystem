/* static/js/app.js */

// Wait for the DOM to be fully loaded before running scripts.
document.addEventListener('DOMContentLoaded', function() {
    
    /**
     * Mobile Menu Toggle Functionality
     * * This script handles the opening and closing of the mobile navigation menu
     * when the hamburger icon is clicked.
     */
    
    // Get the button and the menu elements from the DOM.
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    // Check if both elements exist on the page to avoid errors.
    if (mobileMenuButton && mobileMenu) {
        
        // Add a click event listener to the hamburger button.
        mobileMenuButton.addEventListener('click', () => {
            
            // The 'hidden' class is a standard Tailwind CSS class that sets display: none.
            // Toggling this class will show or hide the menu.
            mobileMenu.classList.toggle('hidden');
        });
    }
});
