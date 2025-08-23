console.log("HAA Website loaded successfully");

// Mobile Menu Functionality
document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.getElementById('menu-toggle');
  const menu = document.querySelector('.menu');
  const dropdowns = document.querySelectorAll('.dropdown');

  // Toggle mobile menu
  if (menuToggle && menu) {
    menuToggle.addEventListener('click', function() {
      menu.classList.toggle('active');
      
      // Toggle hamburger icon animation
      const icon = menuToggle.querySelector('i');
      if (icon) {
        icon.classList.toggle('fa-bars');
        icon.classList.toggle('fa-times');
      }
      
      // Close all dropdowns when menu is toggled
      dropdowns.forEach(dropdown => {
        dropdown.classList.remove('active');
      });
    });
  }

  // Handle dropdown menus on mobile
  dropdowns.forEach(dropdown => {
    const dropdownLink = dropdown.querySelector('a');
    
    if (dropdownLink) {
      // Function to handle dropdown toggle
      function handleDropdownClick(e) {
        // Check if we're on mobile/tablet screen
        const isMobile = window.innerWidth <= 768;
        
        // On mobile screens, prevent default link behavior for ALL dropdown links
        if (isMobile) {
          e.preventDefault();
          e.stopPropagation();
          
          console.log('Mobile dropdown clicked:', dropdownLink.textContent); // Debug log
          
          // Close other dropdowns
          dropdowns.forEach(otherDropdown => {
            if (otherDropdown !== dropdown) {
              otherDropdown.classList.remove('active');
            }
          });
          
          // Toggle current dropdown
          dropdown.classList.toggle('active');
          
          console.log('Dropdown toggled, active:', dropdown.classList.contains('active')); // Debug log
        }
        // On desktop, allow normal link behavior (let the link work normally)
      }
      
      // Add both click and touchstart event listeners for better mobile support
      dropdownLink.addEventListener('click', handleDropdownClick);
      dropdownLink.addEventListener('touchstart', function(e) {
        // For touch devices, we want the same behavior as click
        if (window.innerWidth <= 768) {
          handleDropdownClick(e);
        }
      });
    }
  });

  // Close mobile menu when clicking outside
  document.addEventListener('click', function(e) {
    if (window.innerWidth <= 768) {
      const isClickInsideMenu = menu.contains(e.target);
      const isClickOnToggle = menuToggle.contains(e.target);
      
      if (!isClickInsideMenu && !isClickOnToggle && menu.classList.contains('active')) {
        menu.classList.remove('active');
        dropdowns.forEach(dropdown => {
          dropdown.classList.remove('active');
        });
      }
    }
  });

  // Handle window resize to clean up mobile menu state
  window.addEventListener('resize', function() {
    if (window.innerWidth > 768) {
      menu.classList.remove('active');
      dropdowns.forEach(dropdown => {
        dropdown.classList.remove('active');
      });
    }
  });

  // Back to Top Button Functionality
  const backToTopButton = document.getElementById('backToTop');
  
  if (backToTopButton) {
    // Show/hide button based on scroll position
    window.addEventListener('scroll', function() {
      if (window.pageYOffset > 300) {
        backToTopButton.classList.add('show');
      } else {
        backToTopButton.classList.remove('show');
      }
    });

    // Smooth scroll to top when button is clicked
    backToTopButton.addEventListener('click', function() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
});
